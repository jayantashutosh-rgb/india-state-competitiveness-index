# Data Readiness Report
India State Competitiveness Index (ISCI)

Phase 0, Data Audit
Version 1.0
Date: 10 July 2026

---

## Purpose

I checked the nine source files in the project knowledge before writing any code.
This document reports the state of each file: usable, needs preparation, or not
usable, with the reason.

All findings come from the nine files only. I did not use any external or online
source.

Do not start ETL until the two items under Open decisions are settled.

## Scope

I checked each file on three separate points:

- File integrity: is the file intact and the correct file?
- Extraction quality: how reliably can I read the values out of it?
- Data availability: does it hold the state-level data we need?

These are independent. A file can be intact but hold no relevant data. A file can
hold relevant data that is hard to extract.

## Status labels

- Ready: has the required state-level data, extracts reliably.
- Partially ready: has relevant data, but extraction is hard or coverage is
  incomplete.
- Reference only: intact file, no state values. Useful for definitions or method.
- Unusable: broken, empty, or wrong file.

## File assessments

### RBI Handbook of Statistics on Indian States 2024-25
Status: Ready. Primary source.

The PDF-to-markdown conversion held up well. Table titles, year headers, and
state rows are intact. I read the data rows directly for Table 8 (state-wise
unemployment rate, rural male block, from 1993-94) and Table 19 (per capita net
state domestic product). I have seen Table 9's title but not its rows. The file
has an estimated 170-plus state-wise tables (Estimated; the highest table number
seen is 174). They cover demography and
health, education, employment, poverty, per capita NSDP, factories and capital
(ASI), small-scale industry, power, roads, railways, telephones, bank deposits
and credit, and state finances. This covers most dimensions the index needs.

Extraction notes:
- Numbers use the Indian grouping format (1,53,904).
- Some state names wrap onto a second line.
- Long tables split across pages, marked (Contd.) or (Concld.). We must join them.
- Missing values show as a dot or a dash.
- Some values carry a footnote asterisk.

### RBI Handbook of Statistics on the Indian Economy 2023-24
Status: Partially ready. Mostly national, but it has the state income tables.

Table 5 and Table 6 give Net State Domestic Product by state, at current and
constant prices, from 1993-94 to 2023-24. Tables 9 and 10 give per capita NSDP.
In these tables the states run across the top as columns, not down the side as
rows. Each table also stacks several base-year blocks (1980-81, 1993-94,
1999-2000, 2004-05, and later) across many pages. We can recover the data, but it
takes care. We must not mix two base years in one series.

This is the fullest state income series we have. It partly covers the missing
GSDP file. Note that NSDP is net, not gross, so it is not the same as GSDP.

### Ministry of MSME Annual Report 2025-26
Status: Partially ready. Mostly narrative, with one usable state table.

Most of the file is scheme descriptions and office-address lists. It has one
state-wise Udyam registration table. The columns appear to be micro, small,
medium, and total by state (Inference; the header row is not yet read). I checked
the totals and they add up. For Karnataka: 48,40,286 + 31,489 + 2,293 = 48,74,068
(Verified). The counts are usable. To confirm at extraction: the header row and
the reference date.

### DPIIT / Startup India Annual Report 2025-26
Status: Partially ready, with a gap.

The file has two useful items. First, the national count of DPIIT startup
recognitions by financial year, 2016-17 to 2025-26. This is clean but not
state-level. Second, state-wise IEM filings (Industrial Entrepreneurs Memoranda)
with proposed investment. This is state-level.

The file has no clean state-wise count of recognised startups. I searched for it
and did not find it. We need that count for the innovation dimension, and the CSV
meant to supply it is broken (see below). The IEM data is usable, but it measures
investment intent, not startup counts.

### Startup India State-wise Dataset (CSV)
Status: Unusable.

The file is 131 bytes on one line. It holds an error message, not data:
ResponseDTO(status=true, message=Session Expired, data=null, list=null). The
session expired during export, so nothing came through. It has zero rows.
Download it again after a fresh login and re-upload it.

### State-wise GSDP Dataset (Excel)
Status: Unusable. Wrong file.

The file opens but has no GSDP data. Sheet 1 is a 64-row log of MoSPI website
updates, circulars, orders, and links. Sheet 2 is empty. I checked both. We need
the correct state-wise GSDP file. The RBI NSDP tables partly cover the same
ground, but net income is not gross GSDP. This is one of the two decisions below.

### PLFS PDF (Changes in PLFS from 2025)
Status: Reference only.

The file is intact but is a methodology note on changes to the labour survey from
2025. It has no state-wise labour tables. We do not need them here anyway. The
state unemployment figures are already in the RBI States Handbook (Tables 8 and
9), which use PLFS. Cite this file for method. Do not treat it as a data source.

### Monthly Infrastructure Performance Review, June 2025 (PDF)
Status: Partially ready. Poor fit.

The file reads cleanly and has some state and plant-level figures for power,
refineries, and similar sectors. It covers one month at plant and sector level,
not a multi-year view of state infrastructure. The RBI States Handbook
infrastructure tables fit a structural index better. Keep this file in reserve.
Use it only for a specific recent-month question.

### SDG National Indicator Framework 2026
Status: Reference only.

The file is a definitions and metadata framework. For each indicator it gives the
formula, unit, periodicity, level of disaggregation (State/UT), and data source.
It does not list state values. For those it points to external sources, which we
are not using. It cannot supply numbers to the index. It is useful for matching
our indicators to SDG definitions.

## Open decisions

Both items block the start of ETL.

1. Output measure. Either re-upload the correct state-wise GSDP file, or agree to
   use RBI Net State Domestic Product instead. NSDP is net, not gross. This
   changes how we describe the index later. I will not swap one for the other on
   my own.

2. Startup counts. Re-upload a working state-wise startup CSV. Until then we have
   no per-state startup counts for the innovation dimension. The DPIIT IEM data is
   available, but it is a different measure.

## Summary

We can build the index mainly on the RBI States Handbook. The RBI Economy Handbook
gives the income series. The MSME report gives the Udyam counts. Two intended
files, GSDP and the startup CSV, are unusable as supplied and need re-upload. The
PLFS and SDG files are reference material, not data. The infrastructure report is
optional. ETL waits until the two decisions are made and the three Phase 0
documents are approved.
