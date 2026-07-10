# Data Dictionary
India State Competitiveness Index (ISCI)

Phase 0, Data Audit
Version 1.0
Date: 10 July 2026

---

## How to read this file

This dictionary lists the candidate variables found during the Phase 0 audit,
grouped by source. It is not the final variable list; we pick those in Phase 3. It
records what exists and how far I have checked each item.

Every entry carries one of four verification statuses:

- Verified. I read the actual data rows. Structure, states, years, and units are
  confirmed from the source.
- Partially Verified. I read part of it, but not all. For example, one block of a
  multi-block table, or rows whose header or year labels I have not confirmed.
- Not Yet Verified. I have seen the table title only. No rows read. This does not
  mean the data is bad, only that we have not checked it yet.
- Unavailable. The data is not present in the project knowledge.

Where a statement is not direct evidence, it is labelled: Estimated for an
approximation, Inference for a reasoned guess.

Scope note. The RBI States Handbook holds an estimated 170-plus tables (Estimated;
the highest number seen is 174). I captured titles for Tables 1 to 19 and 100 to
174. Tables 20 to 99 are not catalogued yet. Full cell-level checks happen during
ETL.

---

## Source A: RBI Handbook of Statistics on Indian States 2024-25

### Verified

**Per capita Net State Domestic Product** — Table 19. Current prices, base
2011-12. Unit: rupees. Level: state and UT. I read the rows directly; states and
year columns line up. Missing values show as a dot or dash, some with an asterisk.

**State unemployment rate, rural male block** — Table 8. Years 1993-94 through
2023-24. Unit: per 1,000 persons. Level: state and UT. I read this block directly;
rows are clean and every state is present.

### Partially Verified

**State unemployment rate, remaining blocks** — Table 8 holds several blocks by
sector and sex (rural male, rural female, urban, and so on). I read only the rural
male block. The others share the same layout (Inference) but are not read.

### Not Yet Verified (title seen, rows not read)

- Unemployment rate, second usual-status variant — Table 9.
- Health and demography — birth rate, death rate, infant mortality rate, maternal
  mortality ratio, total fertility rate, life expectancy, natural population
  growth rate, anaemia among children and pregnant women, doctors and specialists,
  government hospitals and beds, public expenditure on health. Tables 2 to 7, 11,
  and 14 to 18.
- Education — gross enrolment ratio, gender parity index of GER. Tables 1 and 12.
- Poverty — multidimensional poverty index. Table 10.
- Tourism — domestic tourist visits. Table 13.
- Prices and wages — CPI inflation (general, food, fuel and light, housing),
  average daily rural wage rates. Tables 108 to 115.
- Industry (ASI) — factories, fixed, working, physical working, productive and
  invested capital, workers, persons engaged, emoluments, input, gross output, net
  and gross value added, capital formation, employees, mandays. Tables 116 to 133.
- Small-scale industry — units, investment, production, employment. Tables 134 to
  137.
- Power — per capita availability, availability, installed capacity, requirement,
  supply position, grid-interactive renewable capacity, transmission and
  distribution losses. Tables 138 to 143 and 148.
- Transport and communication — national highways, railway route, roads, state
  highways, telephones per 100, PMGSY roads. Tables 144 to 147, 149, 150.
- Schools infrastructure — Table 151.
- Banking — bank offices, credit-deposit ratio, deposits, credit, credit to
  agriculture and industry, personal loans, and the same set for regional rural
  banks. Tables 152 to 163.
- State finances — gross fiscal deficit, revenue deficit, revenue expenditure,
  primary deficit, own tax and non-tax revenue, interest payments, pension,
  capital receipts, capital expenditure, capital outlay. Tables 164 to 174.
- Environment — afforestation, tree cover, rainfall, cold and heat wave days,
  groundwater extraction. Tables 100 to 104 and 107 (105 and 106 not observed in
  this pass).

### Not catalogued yet

Tables 20 to 99. Titles not captured in this pass. To be inventoried before or
during ETL.

---

## Source B: RBI Handbook of Statistics on the Indian Economy 2023-24

### Verified

**Net State Domestic Product, current prices** — Table 5. Years 1993-94 to
2023-24. Unit: rupees crore. Level: state and UT. I read the rows directly. Note
the layout: states are columns, not rows, and base years (1980-81, 1993-94,
1999-2000, 2004-05, and later) are stacked. Each base year stays in its own
series.

### Not Yet Verified

- Net State Domestic Product, constant prices — Table 6. Title seen. Assumed to
  share Table 5's span and layout (Inference); not read.
- Per capita Net State Domestic Product — Tables 9 and 10. Unit: rupees. Title
  seen, rows not read.

National macroeconomic series also sit in this handbook. They are national, not
state, so they matter for context, not for the index. Not catalogued here.

---

## Source C: Ministry of MSME Annual Report 2025-26

### Verified

**Udyam registrations by state** — state-wise table. Level: state and UT. A
cumulative count, not a yearly series. I read the rows and the totals add up;
Karnataka reads 48,40,286 + 31,489 + 2,293 = 48,74,068.

The columns appear to be micro, small, medium, and total (Inference; the header
row is not read). To confirm at extraction: the header text and the as-of date.

---

## Source D: DPIIT / Startup India Annual Report 2025-26

### Verified

**DPIIT startup recognitions by financial year (national)** — years 2016-17 to
2025-26. Unit: count of recognition certificates. Level: national only. I read the
rows; the 2025-26 figure is as of 31 December 2025 and the printed grand total is
2,07,135.

### Partially Verified

**IEM filings and proposed investment, by state** — Industrial Entrepreneurs
Memoranda. Level: state and UT. Units: count of filings, and proposed investment
in rupees crore. I read state rows across several year columns, so the data is
real and state-level. The year labels on the columns are not confirmed yet.

### Unavailable

**State-wise startup counts.** Not present in this report. Searched and not found.
The file meant to supply it (Source F) is broken.

---

## Source E: SDG National Indicator Framework 2026

Status: Reference only. No state values to catalogue. The file defines indicators
(formula, unit, periodicity, disaggregation, data source) and points to external
sources for the numbers. Useful in Phase 3 for matching our indicators to SDG
definitions.

---

## Source F: Startup India State-wise Dataset (CSV)

Status: Unavailable. The file holds a download error, not data. No variables.
Future work: re-download after a fresh login and re-upload. See the readiness
report for the exact content.

---

## Source G: State-wise GSDP Dataset (Excel)

Status: Unavailable. Wrong file. No GSDP variables. Sheet 1 is a website update
log, Sheet 2 is empty. Planned decision: re-upload the correct file, or use RBI
NSDP as the output measure.

---

## Source H: PLFS PDF (Changes in PLFS from 2025)

Status: Reference only. Methodology note, no data tables, no dictionary entries.
State unemployment values come from Source A, Tables 8 and 9.

---

## Source I: Monthly Infrastructure Performance Review, June 2025

Status: Held in reserve (not an index source). It has some state and plant-level
figures for power, refineries, and related sectors, but only for one month. Not
catalogued as index variables. Revisit only for a specific recent-month question.
