# Feature Engineering Notes (Notebook 03)
India State Competitiveness Index (ISCI)

---

## 1. What this notebook is for

The earlier notebooks pulled numbers out of the PDFs and saved one CSV per table.
This notebook takes those CSVs and turns them into a single table that the index can
use. It makes the state names match, picks one number per state for each indicator,
adds a few new columns calculated from the existing data, and saves one master table.

## 2. How it is different from the extraction work

Notebooks 01 and 02 read the PDFs. That work is about getting numbers out of a
document. This notebook does not open any PDF. It only uses the clean CSVs and
reshapes them. Reading the PDFs and combining the extracted tables are different
tasks, so they are kept in separate notebooks. This keeps each notebook shorter and
easier to maintain.

## 3. The idea behind it

A few small problems have to be fixed before the tables can be joined:

- The same state is written in different ways across tables ("Jammu And Kashmir" in
  one, "Jammu & Kashmir" in another), and some names carry footnote marks like *.
- Each table has many years, but the index needs one number per state.
- Two union territories, Dadra & Nagar Haveli and Daman & Diu, merged into one, so
  older tables list them separately and newer ones together.
- Some numbers we want (population, roads per person) are not printed anywhere. They
  have to be worked out from other numbers.

Once these issues are fixed, all indicators are joined into one master table.

## 4. What each cell does and why

- Setup: finds the project folder and loads pandas so the rest can run.
- Harmonise names: maps every state name to one clean list, and drops rows that are
  not real places (footnote lines, telecom circles). Without this, many rows would
  fail to match during the merge.
- Data quality report: before using the data, it counts how many states each
  indicator covers and which year, so missing coverage is visible before feature
  engineering begins.
- Pick one value per state: for each indicator it selects the latest year with
  sufficient state coverage, and takes one value per state. Counts are added up and
  rates are averaged when a merged territory has two rows. It also saves a small
  table showing which year each indicator used.
- Build features and master table: works out population from state income, then
  factory, MSME and road density and the industry shares, and saves the final table.

## 5. Common questions

### General

Why not use the raw tables directly in the index?
The tables do not line up. State names differ, years differ, and some numbers must
be worked out first. This notebook makes them line up.

Why is this separate from Notebook 02?
Notebook 02 reads PDFs. This one combines clean tables. They are different jobs.

What is the final output?
One file, master_features.csv, with one row per state and one column per indicator,
plus two helper columns (population and per-capita income).

Why is one master table created instead of joining files during the index calculation?
Building one master table keeps feature engineering separate from index calculation.
The index notebook only works with one prepared dataset, which makes debugging much
easier.

Why is the master table saved before building the index?
Feature engineering and index calculation are separate stages. Saving the master
table creates a clean checkpoint that can be reviewed, validated or reused without
running the extraction notebooks again.

### Names

Why do state names need fixing?
Each source writes them a little differently, and some carry footnote marks. If they
do not match exactly, the tables cannot be joined.

What happens to Dadra & Nagar Haveli and Daman & Diu?
They are now one union territory, so both old names map to one name. Where an older
table lists them separately, the two rows are combined.

Why are telecom circles and footnote lines removed?
They are not states. Forcing them into the state list would add wrong rows.

### Years and values

Why not always use the newest year?
The newest year is sometimes provisional and missing for many states. The notebook
picks the latest year that still covers most states.

How is "enough coverage" decided?
It uses a fixed rule: the latest year with at least 90 percent of that indicator's
best coverage. This avoids picking a thin, half-empty year.

Why do different indicators use different years?
Each official table is updated on its own schedule. The year used for each one is
saved in indicator_metadata.csv.

Why is indicator_metadata.csv saved?
It records which year was selected for every indicator, along with its coverage. This
makes it easy to trace every value back to its source.

### Derived features

What is a derived feature?
A number worked out from other numbers, while leaving the original values unchanged.
For example, population comes from total state income divided by income per person.

Why compute density instead of using raw counts?
A big state naturally has more factories than a small one. Dividing by population
makes states comparable.

Why are some derived features based on different years?
Official datasets are updated at different times. Each derived feature uses the same
reference year as the source variables used to calculate it. The selected year is
recorded in indicator_metadata.csv.

How do we know the population figures are right?
The derived values were compared with published population figures for a few states
to make sure the calculations were reasonable.

### Missing data

Why are some cells empty?
The source does not report that number for that state. Life expectancy, for example,
is published only for the larger states.

Are missing values filled in with guesses?
No. A missing value stays empty until an official value is available.

### Next

What happens after this notebook?
Notebook 04 builds the index. It normalises the indicators, calculates the final
score for each state, and produces the ranking.
