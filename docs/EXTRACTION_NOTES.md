# PDF Extraction Notes
India State Competitiveness Index (ISCI)

---

## 1. Why this notebook exists

Our main data comes from the RBI Handbook, which is a PDF. A PDF is made for people
to read, not for a computer to use. The numbers we need sit inside printed tables.
Before we can analyse anything, we have to pull those numbers out into a clean table
of rows and columns that Python can use.

## 2. How it reads the PDF

- First, the notebook reads the PDF and extracts its text and page layout.
- Then it uses small functions to find a table and read its rows.
- Most tables have states down the side and years across the top. These are simple
  to read.
- A few tables are printed sideways (states across the top) with no lines between
  the cells. Plain text loses the alignment there, so the parser uses the exact
  position of each number on the page (its x and y location) to decide which state
  and which year it belongs to.
- After reading a table, the notebook checks a few of its numbers against the
  printed PDF.

## 3. Why this step is needed

Without it, we would copy thousands of numbers by hand from a 472-page PDF. That is
slow and easy to get wrong. Doing it with code is fast, exact, and repeatable.
Anyone using the same source PDF can run Notebook 01 again and reproduce the same
processed output.

## 4. What the notebook handles

The parser is designed to read these kinds of data: education (enrolment), health
(life expectancy), jobs (unemployment), power, roads, telephones, banking, state
income, and industry (factories, capital formation, manufacturing). It is also built
to handle the hard cases: sideways tables, a table with nested columns, years that
get joined together in the text, missing values, and a national "All-India" total
row.

Verified implementation: the current notebook extracts, validates and saves three
tables: factories, gross fixed capital formation and enrolment. Their spot-checks
match.

The parser is intentionally built as a reusable extraction engine rather than a
collection of table-specific scripts.

Planned next: the other tables listed above are read by the same parser, but are
extracted and saved in a later notebook.

## 5. How it works

- It uses a library called pdfplumber to read the PDF.
- It uses reusable functions to locate tables, extract rows, clean values and
  validate the output.
- For the sideways and borderless tables, it reads the position of each number and
  matches it to the correct column.
- Some headers are too messy for the code to read on its own: names wrap across
  lines, and "Uttar Pradesh" and "Uttarakhand" look almost the same to a program. So
  the correct order of states is kept in a small, human-checked configuration
  (verified once by a person), and the code handles only the positions of the
  numbers.
- Every function is built to stop with a clear error if something looks wrong: a
  missing value, an extra column, or a count that does not match. It does not guess.

## 6. Frequently Asked Questions (FAQ)

### General

**Why not just copy-paste the numbers?**
The RBI Handbook has hundreds of pages and thousands of numbers, so copying by hand
is slow and easy to get wrong. Copy-paste also loses the layout, and some tables
have no borders. Reading with code is fast and works the same way every time.

**Why do we use pdfplumber?**
pdfplumber gives both the text and the position (x and y) of every word and number.
Some tables have no borders, so we need those positions to know which value belongs
to which state and year.

**Why not use OCR?**
OCR is useful when a PDF contains scanned images. The RBI Handbook already contains
digital text, so reading it directly is more accurate than recognising text from
images.

**Why not use AI to extract the tables?**
AI can help explore documents, but research data should be extracted using
deterministic code that produces the same result every time. This makes the process
reproducible and easy to validate.

**Why not use existing PDF table extraction tools?**
Many PDF extraction tools work well on regular tables. The RBI Handbook contains
tables with merged headers, wrapped text, borderless layouts, and transposed
structures that require custom handling. Building a dedicated parser gives better
control, validation, and reproducibility.

**Why not convert the PDF to Excel first?**
Converting the PDF to Excel introduces another processing step that may change the
table structure or formatting. Reading directly from the official PDF keeps the
workflow simpler and easier to reproduce.

**Why do we extract only the tables we need?**
The handbook contains many tables that are outside the scope of this project.
Extracting only the required tables keeps the workflow faster, easier to validate,
and simpler to maintain.

### Parser

**What is a parser?**
A parser is a program that reads data in one format and converts it into another
format that is easier for a computer to use. Here, the parser reads PDF tables and
converts them into structured rows and columns. The same parser can be reused for
many tables instead of writing new code for every table.

**Why are some tables hard?**
A few are printed sideways, with no cell borders and with state names split across
lines. Plain text cannot tell which number belongs to which state, so the parser
uses the position of each number on the page instead.

**Why do some tables need a configuration?**
Some state names wrap across several lines or look almost the same to a computer. A
small configuration stores the verified state order once, while the parser still
validates every value before accepting it.

**Why do we build reusable functions?**
Many RBI tables follow similar layouts. Reusable functions reduce duplicate code,
make testing easier, and let the same extraction engine work on multiple tables. If
one part needs to change, we update that function instead of rewriting the notebook.

**Why does the parser stop instead of guessing?**
Wrong data is more dangerous than missing data. If something does not look correct,
the notebook raises an error and stops. This prevents incorrect values from entering
the project without anyone noticing.

**Can the parser be used for other government PDFs?**
Many of the functions are reusable because they work with tables in general. Some
reports may still need a different configuration because each publication uses a
different layout.

**What happens when a table continues on another page?**
The parser joins all pages that belong to the same table before processing the data.
It treats them as one table instead of several separate pieces.

### Data

**Why do we save the extracted tables as CSV files?**
CSV files are simple, portable, and work with almost every data tool. They open in
Python, SQL, Excel, Power BI, and many other programs without changing the data.

**What is tidy data?**
Tidy data means each row is one observation and each column is one variable. This
format is much easier to analyse using pandas, SQL, statistics, and machine learning.

**Why do we keep raw and processed data in different folders?**
The data/raw folder always holds the original source files. The data/processed folder
holds the cleaned data produced by the notebook. Keeping them separate protects the
original evidence.

**Why do we keep the original PDF unchanged?**
The original PDF is the evidence for the project. The notebook only reads it and
never edits or overwrites it, so anyone can go back to the official document and
verify a number.

**Why keep "All-India" while parsing and remove it later?**
The All-India total helps confirm that the whole table is read. It is removed before
analysis because the project studies individual states, not the national total.

**What is feature engineering?**
Feature engineering means creating a new variable from existing data without changing
the original values. For example, factory density is calculated from the number of
factories and the state population.

### Reliability

**What happens to a missing value?**
The code records it as missing (empty), not as a guess. Filling a gap with a guessed
number would make the data less trustworthy. Real gaps stay empty, for example a
small union territory that stopped reporting after it merged with another.

**How do we check the data is correct?**
For each finished table, selected values are compared against the printed PDF. The
parser also performs automatic validation before the table is accepted.

**Why do we validate the data before saving it?**
Only validated tables are written to the data/processed folder, so every later step
in the project starts with trusted data. Finding an error early is much easier than
finding it after thousands of rows are processed.

**What happens if RBI changes the table layout in a future edition?**
The validation checks are designed to fail instead of silently producing incorrect
data. If the layout changes, the parser or its configuration can be updated before
any new data is accepted.

**Can I check where a number came from?**
Yes. Every extracted value can be traced back to the original RBI table and page,
which keeps the process transparent and easy to verify.

**Why does the project use local files instead of downloading data automatically?**
Local files ensure that everyone works with exactly the same version of the official
documents. It also makes the project reproducible even without an internet connection.

**How long does the extraction take?**
It depends on the size of the PDF and the number of tables. Even so, automated
extraction is much faster and more reliable than entering thousands of values by hand.

**How do we know the notebook is reproducible?**
Anyone with the same source PDF can run Notebook 01 and get the same processed
tables. The notebook follows the same steps every time and does not depend on manual
editing.
