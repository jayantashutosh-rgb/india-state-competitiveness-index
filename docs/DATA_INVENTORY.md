# Data Inventory
India State Competitiveness Index (ISCI)

Phase 0, Data Audit
Version 1.0
Date: 10 July 2026

---

## About this document

This is the master catalogue of the source files in the project knowledge, one
entry per file. Each entry has a compact facts block, then a short note on what we
can take from the file and what to watch for.

Two points that apply to every entry, stated once here:

- The final variable list is not decided yet. That is Phase 3 (indicator
  selection). This inventory records what each file holds, not what we have
  chosen.
- The "Status" field here is a readiness label (Ready, Partially ready, Reference
  only, Unusable). It answers "can we use this file". Variable-by-variable
  verification status (Verified, Partially Verified, Not Yet Verified, Unavailable)
  is in DATA_DICTIONARY.md.

Statements are labelled where they are not direct evidence: Estimated for
approximations, Inference for reasoned guesses. I update this file when we add a
source or confirm a detail.

---

## 1. RBI Handbook of Statistics on Indian States 2024-25

Status: Ready
Source: Reserve Bank of India
Coverage: States and UTs
Years: Varies by table; many run to 2023-24 or 2024-25
Phase: 4 to 11
Stored as: RBI Handbook of Statistics on Indian States 2024-25.md

This is the primary source for most of the indicators used in the index. It holds
an estimated 170-plus state-wise tables (Estimated; the highest table number seen
is 174), covering demography and health, education, employment and unemployment,
poverty, per capita NSDP, factories and capital from the ASI, small-scale
industry, power, transport, telephones, bank credit and deposits, and state
finances. These map to most of Porter's dimensions: factor conditions (labour,
infrastructure, finance), related and supporting industries (ASI, small-scale
industry), and government (state budgets). They support the core questions of
which states are most competitive and which convert public spending into
outcomes.

Extraction watch-list: numbers use the Indian grouping style (1,53,904); some
state names wrap to a second line; long tables split across pages under (Contd.)
and (Concld.) and must be rejoined; missing values show as a dot or a dash; some
figures carry a footnote asterisk. Each table has its own year span, so panels
align one indicator at a time.

## 2. RBI Handbook of Statistics on the Indian Economy 2023-24

Status: Partially ready
Source: Reserve Bank of India
Coverage: States and UTs for the income tables; national elsewhere
Years: State NSDP 1993-94 to 2023-24
Phase: 4 to 11
Stored as: HANDBOOK OF STATISTICS ON THE INDIAN ECONOMY 2023-24 RBI.md

Most of this book is national, but it carries the state income series. Tables 5
and 6 give Net State Domestic Product by state at current and constant prices, and
Tables 9 and 10 give the per capita version, in rupees crore. The layout is
awkward: states sit across the top as columns, and each table stacks several
base-year blocks (1980-81, 1993-94, 1999-2000, 2004-05, and later) across many
pages. The data is recoverable, but the extraction must transpose it and keep each
base year in its own series.

This is the longest income series available and partly stands in for the missing
GSDP file. Planned decision: NSDP is a net figure and GSDP is gross, so using it
as the output measure is a call recorded in the readiness report, not something
settled here.

## 3. Ministry of MSME Annual Report 2025-26

Status: Partially ready
Source: Ministry of MSME
Coverage: States and UTs (Udyam table)
Years: 2025-26 report; cumulative snapshot
Phase: 4 to 11
Stored as: Annual Report of Ministry of MSME (2025–26).md

The report is mostly written material, scheme write-ups and lists of field
offices. The part we want is one table: Udyam registrations by state. The columns
appear to be micro, small, medium, and total (Inference; the header row is not yet
read). The row totals add up, for example Karnataka: 48,40,286 + 31,489 + 2,293 =
48,74,068 (Verified). These counts speak to the small-business base of each state,
under related and supporting industries.

To confirm at extraction: the header text and the date the cumulative count runs
to.

## 4. DPIIT / Startup India Annual Report 2025-26

Status: Partially ready
Source: DPIIT
Coverage: National (startup counts); States and UTs (IEM)
Years: Recognitions 2016-17 to 2025-26
Phase: 4 to 11
Stored as: Startup IndiaDPIIT (State-wise Startup Data)PDF_compressed.md

Two useful items are here. The national count of DPIIT startup recognitions by
financial year is clean but not broken down by state. The state-wise IEM filings
(Industrial Entrepreneurs Memoranda) with proposed investment are genuinely at
state level.

What is missing is a state-wise count of recognised startups; I searched for that
table and did not find it. That count is what the innovation dimension needs, and
the CSV meant to carry it is broken (entry 5). The IEM figures track investment
intent, which is a different question from how many startups a state has.

## 5. Startup India State-wise Dataset (CSV)

Status: Unusable
Source: Startup India / DPIIT portal
Coverage: None
Years: None
Phase: Pending re-upload
Stored as: files/733b6216-47b8-4c7e-8376-35995991a807.csv

There is no data in this file. It is 131 bytes on a single line, and that line is
a download error rather than a record: ResponseDTO(status=true, message=Session
Expired, data=null, list=null). The session timed out mid-export.

Future work: download it again after a fresh login and re-upload. It was meant to
supply state-wise startup counts for the innovation dimension, so that gap stands
until then.

## 6. State-wise GSDP Dataset (Excel)

Status: Unusable (wrong file)
Source: Intended MoSPI GSDP
Coverage: None relevant
Years: None relevant
Phase: Pending re-upload or decision
Stored as: files/efc4f8ba-c50c-4885-9af8-9ef3761ded0e.xlsx

The file opens, but there is no GSDP in it. The first sheet is a 64-row log of
MoSPI website updates, circulars, and links; the second sheet is blank.

Planned decision: re-upload the correct state-wise GSDP file, or use RBI NSDP as
the output measure. The RBI NSDP tables cover part of the same ground, but net
income is not gross output, so this is a call for you to make.

## 7. PLFS PDF (Changes in PLFS from 2025)

Status: Reference only
Source: MoSPI, National Statistics Office
Coverage: National methodology
Years: 2025
Phase: Methodology reference (Phase 15)
Stored as: files/9b5f7421-e0aa-48e2-8e14-d5bee78846bc.pdf

This is a methodology note on how the labour survey changed from 2025. It has no
state labour tables, and we do not need them here: the state unemployment figures
already sit in the RBI States Handbook (Tables 8 and 9), which draw on PLFS. We
keep this file to cite when we explain method, not as a source of numbers.

## 8. Monthly Infrastructure Performance Review, June 2025 (PDF)

Status: Partially ready (poor fit)
Source: Government of India
Coverage: National; some state and plant figures
Years: June 2025
Phase: Optional, on demand
Stored as: files/a712189a-634b-4400-8e04-e44dfac022a2.pdf

The file reads cleanly and has a few state and plant-level numbers, mainly for
power and refineries. The limit is what it is: a one-month snapshot at plant and
sector level, not a multi-year picture of a state's infrastructure. The RBI States
Handbook tables serve a structural index far better. Held in reserve for a
specific recent-month question.

## 9. SDG National Indicator Framework 2026

Status: Reference only
Source: MoSPI, National Statistics Office
Coverage: Defines State/UT level; lists no values
Years: 2026
Phase: Phase 3 reference
Stored as: Sustainable Development Goals – National Indicator Framework Progress Report 2026.md

This file describes indicators rather than reporting them. Each entry gives the
formula, unit, periodicity, the level it can be split to, and where the data
lives. It does not print the state values themselves; for those it points to
external sources we are not drawing on. It adds no numbers to the index, but it is
a good reference for matching our indicators to accepted SDG definitions when we
settle the indicator list in Phase 3.
