# India State Competitiveness Index (ISCI)

A state-level competitiveness index for India, built from official government data and
based on Michael Porter's Diamond framework. Version 1.0 scores and ranks states and
union territories on 11 indicators, and tests how stable that ranking is. Version 2.0 then
explains the index through analysis, interpretation, clustering, gap analysis, priorities
and scenarios.

## Project at a glance

- 2 official government data sources
- 470+ page RBI handbook processed
- 17 indicator tables extracted
- 11 final competitiveness indicators
- 15 Jupyter notebooks (5 build the index, 10 explain it)
- 3 reusable Python modules
- 33 states and union territories ranked
- 3 robustness checks
- 3 state types found by clustering
- 9 research and reflection documents
- Fully reproducible pipeline

## Overview

The index takes public data from the RBI Handbook of Statistics on Indian States and the
MSME Annual Report, turns it into 11 comparable indicators, and combines them into one
competitiveness score per state. Each step, from reading the PDFs to the final ranking,
is done in a notebook so the whole thing can be re-run and checked.

## Problem

There is a lot of official data on Indian states, but it sits in separate tables, in PDF
form, in different units and different years. There is no simple, open, reproducible way
to compare states on competitiveness using only official sources and a recognised
framework. This project builds one.

## Why this project

- It uses only official government data, with every source and choice written down.
- It applies a well-known framework (Porter's Diamond) instead of an arbitrary mix of
  indicators.
- It is fully reproducible: the notebooks run in order and produce the same result.
- It separates building the index from testing it, so the ranking can be trusted.

## Porter's Diamond framework

Michael Porter's Diamond explains why some places are more competitive than others
through four determinants:

1. Factor Conditions — skills, infrastructure, capital and other inputs.
2. Demand Conditions — the size and nature of local demand.
3. Related & Supporting Industries — the presence of suppliers and connected industries.
4. Firm Strategy, Structure & Rivalry — how firms are organised and how they compete.

Version 1.0 operationalises the two determinants that can be measured cleanly from the
available official data: Factor Conditions and Related & Supporting Industries. Demand
Conditions and Firm Strategy are left for a later version, because the data needed to
measure them at the state level is not reliable yet. This choice is recorded in the docs.

## Data sources

- RBI, Handbook of Statistics on Indian States 2024-25.
- Ministry of MSME, Annual Report (Udyam registrations).

Other official documents were reviewed during the audit but are not used in Version 1.0.
The reasons are recorded in `docs/DATA_INVENTORY.md` and `docs/DATA_DECISIONS.md`.

## Workflow

The project runs in two stages, one notebook per job.

### Version 1.0 — build the index

| Notebook | Job |
|----------|-----|
| 01 — PDF text extraction | Read the RBI handbook PDF and save its text. |
| 02 — Indicator extraction | Pull each indicator table into a clean CSV. |
| 03 — Feature engineering | Standardise state names, pick a year per indicator, build density and share features, and make one master table. |
| 04 — Index construction | Scale the indicators, combine them into a score, and rank the states. |
| 05 — Validation and sensitivity | Test how stable the ranking is under different choices. |

The reusable parsing code sits in `src/parser.py` and `src/entities.py`. The scoring code
sits in `src/scoring.py`, so Notebooks 04, 05 and the Version 2.0 notebooks score states the
same way.

### Version 2.0 — explain the index

| Notebook | Question it answers |
|----------|---------------------|
| 06 — Exploratory data analysis | What does the data look like? |
| 07 — State profiles | How does each state perform? |
| 08 — Porter's Diamond interpretation | Why do states perform this way? |
| 09 — Comparative analysis | How do groups of states differ? |
| 10 — State clustering | What state types exist? |
| 11 — Gap analysis | Where are the biggest gaps? |
| 12 — Development priorities | Which areas deserve the highest priority? |
| 13 — Scenario analysis | What happens if one priority gap is closed? |
| 14 — Research findings | What are the main findings? |
| 15 — Final report | What is the overall summary? |

### Research workflow

```
Official PDFs
      ↓
Data extraction               (Notebooks 01–02)
      ↓
Cleaning & feature engineering (Notebook 03)
      ↓
Index construction            (Notebooks 04–05, Version 1.0)
      ↓
Analysis                      (Notebooks 06–11, Version 2.0)
      ↓
Interpretation & priorities   (Notebooks 08, 12–13)
      ↓
Reports & documentation       (Notebooks 14–15, docs)
```

## Folder structure

```
india-state-competitiveness-index/
├── data/
│   ├── raw/            official source PDFs (not edited)
│   └── processed/      extracted CSVs and the master feature table
├── notebooks/          01 to 15, the full pipeline
├── src/                parser, entity list, scoring functions
├── docs/               methodology, data decisions, and a note for each notebook
├── results/            Version 1.0 scores, rankings, and validation notes
├── version2/
│   ├── reports/        Version 2.0 reports (analysis, priorities, findings)
│   └── figures/        charts from the analysis
├── THESIS.md           full research narrative
├── FAQ.md              quick answers and repository map
└── README.md
```

Other top-level documents (Final Report, Executive Summary, Research Decisions, Project
Philosophy, Lessons Learned, Editorial, Why Python Mattered) are listed below.

## Results

Version 1.0 scores 33 states and union territories. Three union territories fall below
the coverage rule and are not ranked.

Top 10:

| Rank | State | Score |
|------|-------|-------|
| 1 | Goa | 0.610 |
| 2 | Tamil Nadu | 0.605 |
| 3 | Gujarat | 0.594 |
| 4 | Puducherry | 0.565 |
| 5 | Telangana | 0.523 |
| 6 | Andhra Pradesh | 0.507 |
| 7 | Punjab | 0.506 |
| 8 | Maharashtra | 0.505 |
| 9 | Himachal Pradesh | 0.489 |
| 10 | Haryana | 0.480 |

Bottom 5:

| Rank | State | Score |
|------|-------|-------|
| 29 | Andaman & Nicobar Islands | 0.254 |
| 30 | Bihar | 0.245 |
| 31 | Meghalaya | 0.223 |
| 32 | Nagaland | 0.204 |
| 33 | Arunachal Pradesh | 0.198 |

The full ranking is in `results/competitiveness_index.csv`, and a short readable version
is in `results/RESULTS.md`.

## Key findings

- States that are strong on industry and investment sit near the top; states with almost
  no industrial base sit at the bottom.
- The scores are close together, so the order of states is more useful than the gap
  between scores.
- The ranking is stable. Changing the unemployment measure, the coverage rule, or the
  scaling method makes very little difference (Spearman correlation of 0.99 or higher in
  each check).

## Documentation

The project keeps its writing separate from its code, so each document has one clear role.

| Document | Role |
|----------|------|
| `version2/reports/executive_summary.md` | Two-minute overview |
| `version2/reports/final_report.md` | Complete results |
| `THESIS.md` | Full research narrative |
| `RESEARCH_DECISIONS.md` | Why each major design choice was made |
| `PROJECT_PHILOSOPHY.md` | Principles followed during the work |
| `LESSONS_LEARNED.md` | What the project taught |
| `EDITORIAL.md` | Why the project matters |
| `WHY_PYTHON_MATTERED.md` | Why these tools were used |
| `FAQ.md` | Quick answers and a map of the repository |

Each notebook also has a plain-language note in `docs/`.

## Reading order

Different readers can take different paths:

- New reader: Executive Summary, then Final Report.
- Researcher: README, then THESIS, then Research Decisions.
- Developer: README, then the notebooks, then Why Python Mattered.
- Student: Executive Summary, then FAQ, then THESIS.

## How to run

The project uses Python 3 and Jupyter.

1. Install the packages:

   ```
   pip install pandas pdfplumber scikit-learn matplotlib seaborn jupyter
   ```

2. Put the source PDFs in `data/raw/` (see the data sources above).

3. Open the notebooks and run them in order, 01 to 15. Each notebook reads what the
   previous one saved, so the order matters.

Outputs are written to `data/processed/`, `results/` and `version2/`.

## Version history

| Version | Purpose |
|---------|---------|
| 1.0 | Build the index |
| 2.0 | Explain the index |

## Future work

Both stages are complete. A later version could:

- Add measures for the remaining two Porter determinants (Demand Conditions and Firm
  Strategy) when reliable state-level data is available.
- Build a multi-year panel to study change over time.
- Add more indicators and an interactive dashboard.
- Automate the annual update when new official reports are published.

Every future improvement should keep the project's principles of transparency,
reproducibility and careful documentation.

## Repository principles

Every result can be traced back to code. Every important decision is documented. Every
limitation is stated openly.

## License

Released under the MIT License. See `LICENSE`.

## Author

Ashutosh Jayant
