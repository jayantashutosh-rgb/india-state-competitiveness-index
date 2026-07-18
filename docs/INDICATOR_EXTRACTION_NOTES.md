# Indicator Extraction Notes (Notebook 02)
India State Competitiveness Index (ISCI)

---

## 1. Why this notebook exists

Notebook 01 built the parser and solved the hardest tables. Notebook 02 uses that
same parser to pull out the remaining indicators the index needs, and saves each one
as a clean CSV in data/processed.

## 2. Why this was not done inside Notebook 01

Notebook 01 focused on building and validating the parser. Once the parser was
stable, the remaining indicator extraction was moved to Notebook 02. Keeping the two
tasks separate makes both notebooks easier to understand and maintain.

## 3. Difference between Notebook 01 and Notebook 02

- Notebook 01 writes the parser functions and handles the three hard tables
  (factories, capital formation, enrolment). The reusable functions now live in
  src/parser.py.
- Notebook 02 imports those functions from src/parser.py and extracts the remaining
  tables. It does not rewrite any parser code.
- In short, Notebook 01 builds the extraction engine and Notebook 02 applies it to
  the remaining tables.

## 4. What each step does

- Setup: finds the project root, loads the text that Notebook 01 saved, and runs one
  quick test (life expectancy) to confirm the parser imports and works.
- Batch extraction: loops over the straightforward tables (life expectancy, power,
  roads, T&D losses, telephones, manufacturing and total value added, per-capita and
  total state income) and saves each as a CSV.
- Unemployment extraction: the unemployment table has separate blocks for rural and
  urban, each split into male, female and overall. This step pulls the rural overall
  and urban overall series and saves both.
- Credit-deposit extraction: saves both versions of the credit-deposit ratio, by
  place of utilisation and by place of sanction.
- MSME extraction: opens a different PDF (the MSME Annual Report) and reads the
  state-wise Udyam registration table. Three union territories whose names wrap
  across lines are added from the verified source values.
- Summary: lists every CSV saved in data/processed with its row and state count.

## 5. Status

Seventeen tables have been extracted, validated and saved in `data/processed`. Their
row counts and selected values have been checked against the source documents.

Planned next: the tables use slightly different state lists, so the first job in
feature engineering (Notebook 03) is to standardise the state names and align every
table to one common list before anything is joined.

## 6. Frequently Asked Questions (FAQ)

### General

**Why keep parser code in src/parser.py instead of copying it into each notebook?**
Copying code into every notebook creates duplicates that drift apart over time.
Keeping it in one file means both notebooks use the same tested functions, and a fix
is made in only one place.

**Why load a saved text file instead of reading the PDF again?**
Notebook 01 already turned the PDF into text and saved it. Reading that text is
faster, and the text does not change, so the results stay the same.

**Why are the indicators extracted into separate files before merging?**
Keeping each indicator separate makes validation easier. Problems can be traced back
to a single source table without affecting the rest of the extracted data. The
tables are merged later during feature engineering.

### Data choices

**Why is unemployment saved as two separate files?**
The source publishes rural and urban unemployment separately and gives no combined
figure. Both are saved now, and the choice of which to use is made later during
feature engineering.

**Why are there two credit-deposit ratio files?**
Place of utilisation is used in the index because it shows where credit is actually
deployed. Place of sanction is kept only as a reference. This is recorded in
DATA_DECISIONS.md.

**Why were three union territories added to the MSME table by hand?**
Their names wrap across two lines in the PDF, so the automatic reader could not
capture them reliably. Their values were read from the source table and checked, and
the addition is recorded in DATA_DECISIONS.md.

### Data quality

**Why do the tables have different numbers of states?**
Each table covers a slightly different set. Life expectancy is published for major
states only. Telephones are reported by telecom circle, not by state. Some tables
include or exclude certain union territories or the All-India total. A few rows with
wrapped names can also drop out. These differences are handled in feature
engineering, where all tables are aligned to one common state list.

**Why does telephones show only 28 rows?**
The telephone table is organised by telecom circle, not by state. Metros like Delhi,
Mumbai, Kolkata and Chennai are separate circles, and some states are grouped
together. Its use is decided in feature engineering.

**How do we know the extracted numbers are correct?**
Each table is checked against the printed source for several values, and the parser
stops with an error if a table does not read cleanly.

### Terms and next steps

**What is a tidy CSV?**
A file where each row is one observation (for example, one state in one year) and
each column is one piece of information. It is easy to analyse in pandas and SQL.

**What is src/parser.py?**
A single Python file that holds the reusable parser functions built in Notebook 01.
Both notebooks import from it.

**What happens after this notebook?**
Feature engineering (Notebook 03): standardise state names, derive population and
density-style features, and select the final column and year for each indicator.
Then the index is built.
