"""
Reusable parser for RBI Handbook tables (India State Competitiveness Index).

These are the generic functions built and validated in Notebook 01. They locate a
table in the extracted PDF text (or PDF word positions) and turn it into a tidy
DataFrame. Table-specific details (page numbers, expected columns, verified state
order) are passed in by the caller as configuration; they are not hardcoded here.
"""

import re
import bisect
from collections import defaultdict

import pandas as pd
import pdfplumber


# --- patterns -------------------------------------------------------------

TABLE_HEADER = re.compile(r"^TABLE\s+(\d+)\s*:", re.MULTILINE)
YEAR_FY = re.compile(r"^\d{4}-\d{2}$")
YEAR_CAL = re.compile(r"^\d{4}$")
NUMBER = re.compile(r"^-?\d[\d,]*(\.\d+)?\*?$")


# --- small helpers --------------------------------------------------------

def is_year(token):
    return bool(YEAR_FY.match(token) or YEAR_CAL.match(token))


def is_value(token):
    return bool(NUMBER.match(token)) or token in {".", "-"}


def clean_number(token):
    """Turn a printed number into a float. Missing markers ('.', '-') become None."""
    if token is None:
        return None
    token = token.strip().rstrip("*")
    if token in {".", "-", ""}:
        return None
    return float(token.replace(",", ""))


# --- locating a table in the extracted text -------------------------------

def locate_table(text, table_number):
    """Return the text block for one table, including its Contd./Concld. pages."""
    headers = [(m.start(), int(m.group(1))) for m in TABLE_HEADER.finditer(text)]
    for i, (start, number) in enumerate(headers):
        if number != table_number:
            continue
        end = len(text)
        for next_start, next_number in headers[i + 1:]:
            if next_number != table_number:
                end = next_start
                break
        return text[start:end]
    return None


# --- general row-oriented parser (states as rows, years as columns) -------

def parse_table(block):
    """Parse a text block where states are rows and years are columns."""
    if block is None:
        return pd.DataFrame(columns=["state", "year", "value"])
    lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
    records = []
    years = None
    for line in lines:
        tokens = line.split()
        low = line.lower()
        if "state/union territory" in low or "state/ut" in low:
            found = re.findall(r"\d{4}-\d{2}", line) or re.findall(r"\d{4}", line)
            if found:
                years = found
            continue
        if tokens and all(YEAR_FY.match(t) for t in tokens):
            years = tokens
            continue
        if years is None or line.upper().startswith("TABLE"):
            continue
        cut = next((i for i, t in enumerate(tokens) if is_value(t)), None)
        if cut is None or cut == 0:
            continue
        state = " ".join(tokens[:cut])
        if state.isupper():          # skip region aggregates (e.g. NORTHERN REGION)
            continue
        values = [t for t in tokens[cut:] if is_value(t)]
        for year, value in zip(years, values):
            records.append((state, year, clean_number(value)))
    df = pd.DataFrame(records, columns=["state", "year", "value"])
    return df.drop_duplicates(["state", "year"]).reset_index(drop=True)


# --- coordinate-based helpers (borderless / transposed tables) ------------

def find_value_columns(words, gap=20):
    """Detect column positions from value words using their right edges.
    Returns (centers, boundaries); boundaries are midpoints between centers."""
    edges = sorted(w["x1"] for w in words if is_value(w["text"]))
    if not edges:
        raise ValueError("no value words found")
    clusters = [[edges[0]]]
    for x in edges[1:]:
        if x - clusters[-1][-1] <= gap:
            clusters[-1].append(x)
        else:
            clusters.append([x])
    centers = [sum(c) / len(c) for c in clusters]
    boundaries = [(centers[i] + centers[i + 1]) / 2 for i in range(len(centers) - 1)]
    return centers, boundaries


def extract_value_rows(page_words, expected_columns, row_filter=None):
    """Ordered value rows for any table with fixed-width numeric columns.
    The detected column count must equal expected_columns. Blanks are kept as None.
    row_filter(top, values) can drop non-data rows."""
    centers, boundaries = find_value_columns(page_words)
    if len(centers) != expected_columns:
        raise ValueError(f"detected {len(centers)} columns, expected {expected_columns}")
    lines = defaultdict(list)
    for w in page_words:
        if is_value(w["text"]):
            lines[round(w["top"])].append(w)
    rows = []
    for top in sorted(lines):
        slots = [None] * expected_columns
        for w in lines[top]:
            idx = bisect.bisect_right(boundaries, w["x1"])
            if 0 <= idx < expected_columns and slots[idx] is None:
                slots[idx] = clean_number(w["text"])
        if any(s is not None for s in slots):
            if row_filter is None or row_filter(top, slots):
                rows.append((top, slots))
    return rows


def split_page_into_blocks(page_words):
    """Split a page into stacked blocks (header_words, body_words).
    Boundaries are real header bands (with letters) or year resets."""
    lines = defaultdict(list)
    for w in page_words:
        lines[round(w["top"])].append(w)

    def classify(top):
        row = sorted(lines[top], key=lambda w: w["x0"])
        if row and YEAR_FY.match(row[0]["text"]):
            return "year", row[0]["text"]
        if any(re.search(r"[A-Za-z]", w["text"]) for w in row):
            return "header", None
        return "other", None

    blocks, header, body, prev_year = [], [], [], None
    for top in sorted(lines):
        kind, y = classify(top)
        if kind == "header":
            if body:
                blocks.append((header, body))
                header, body, prev_year = [], [], None
            header.extend(lines[top])
        elif kind == "year":
            if prev_year is not None and y <= prev_year:
                blocks.append((header, body))
                header, body, prev_year = [], [], None
            body.extend(lines[top])
            prev_year = y
    if body:
        blocks.append((header, body))
    return blocks


def parse_transposed_body(body, boundaries, state_order):
    """Map each year-row's values into columns for a transposed block.
    Empty cells become None; a collision (two values in one column) raises."""
    rows = defaultdict(list)
    for w in body:
        rows[round(w["top"])].append(w)
    records = []
    n_cols = len(state_order)
    for top in sorted(rows):
        words = sorted(rows[top], key=lambda w: w["x0"])
        year_words = [w for w in words if YEAR_FY.match(w["text"])]
        if not year_words:
            continue
        year = year_words[0]["text"]
        slots = [None] * n_cols
        for w in words:
            if not is_value(w["text"]):
                continue
            idx = bisect.bisect_right(boundaries, w["x1"])
            if slots[idx] is not None:
                raise ValueError(f"row {year}: two values in column {idx} ({state_order[idx]})")
            slots[idx] = w["text"]
        for state, token in zip(state_order, slots):
            records.append((state, year, clean_number(token) if token is not None else None))
    df = pd.DataFrame(records, columns=["state", "year", "value"])
    return df.drop_duplicates(["state", "year"]).reset_index(drop=True)


def extract_transposed(pdf_path, table_name, pages, config):
    """Parse a transposed table across pages using per-block configuration.
    config[(table_name, page)] is a list of verified state-name lists, one per
    block on that page."""
    frames = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pages:
            words = pdf.pages[page].extract_words(use_text_flow=False)
            blocks = split_page_into_blocks(words)
            cfg = config[(table_name, page)]
            if len(blocks) != len(cfg):
                raise ValueError(
                    f"page {page}: {len(blocks)} blocks detected, {len(cfg)} configured")
            for (header, body), state_order in zip(blocks, cfg):
                centers, boundaries = find_value_columns(body)
                if len(centers) != len(state_order):
                    raise ValueError(
                        f"page {page}: {len(centers)} columns detected, "
                        f"{len(state_order)} configured")
                frames.append(parse_transposed_body(body, boundaries, state_order))
    return pd.concat(frames, ignore_index=True)
