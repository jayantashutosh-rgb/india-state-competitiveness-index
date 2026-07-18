# Frequently Asked Questions

Short answers to common questions about the project. Where more detail exists, the answer
points to the right document. This page also works as a map of the repository.

## 1. General

**What is this project?**
It is the India State Competitiveness Index (ISCI). It scores and ranks Indian states on how
competitive they are for business, using only official data, and then explains the result. See
final_report.md for the full picture.

**Is this an official government ranking?**
No. It is an independent research project built entirely from official government data.

**Why was it created?**
Official data is spread across long reports in different units and years. There was no simple,
open, reproducible way to compare states. This project builds one. See EDITORIAL.md.

**What question does it answer?**
How competitive are Indian states, and what explains the differences between them?

**Who is it for?**
Students, researchers, analysts and anyone interested in Indian states. It is written in simple
language so any reader can follow it.

## 2. Data and method

**Why only official data?**
So anyone can download the same reports and repeat the work. It keeps the project transparent
and reproducible. See RESEARCH_DECISIONS.md.

**Why Porter's Diamond?**
It is a recognised framework, and its parts can be linked to official indicators. It was chosen
before the data was collected. See THESIS.md, Section 3.

**Why only two of the four parts?**
Only Factor Conditions and Related & Supporting Industries had reliable state-level data. The
other two were left out rather than guessed.

**Why 11 indicators?**
These were the indicators that were reliable, available for most states, and comparable. The
number is not special.

**Why equal weights?**
The data gives no fair basis to weight one indicator above another, so equal weights are the
most honest and easy to check. See RESEARCH_DECISIONS.md.

**Why Min-Max scaling?**
It puts every indicator on a 0 to 1 scale and is easy to explain. Z-score was tested and gave
almost the same ranking.

**Why the 8-of-11 coverage rule?**
A score from too few indicators is not trustworthy. Requiring 8 of 11 is a middle path between
dropping many states and filling in missing values.

**Why K-Means for grouping?**
It is simple and clear, and it worked well on the two measured dimensions. See Notebook 10.

## 3. Findings

**What did the project find?**
Basic conditions explain where a state stands against the average today. Industry explains the
distance to the strongest states. See research_findings.md.

**Which states ranked highest?**
Goa is highest, followed by Tamil Nadu and Gujarat. Arunachal Pradesh is the lowest of the 33
ranked states. Scores run from about 0.20 to 0.61.

**Why are the scores so close together?**
The index measures relative differences between states. The ranking is usually more informative
than the exact score.

**What separates the strong states?**
Mostly the measured industry indicators: factories, manufacturing, investment and small
businesses. The strongest states are far ahead on these.

**What does the middle group mean?**
It is a set of states that are strong on basic conditions but weak on industry, such as Kerala
and Delhi. Industry is the main thing holding them back.

## 4. Interpretation

**Does correlation mean causation?**
No. When two numbers move together, it does not prove one causes the other. The project says
this on purpose.

**Why isn't Demand included?**
There is no direct state-level measure of local demand in the data. It is only described using
income figures as simple proxies, outside the index.

**Why isn't Firm Strategy measured?**
There is no reliable state-level official data for it. It is left as a limit, not filled in.

## 5. Design decisions

**Why Python?**
It made a locked PDF of official data usable, removed hand-copying, and made every step
repeatable. See WHY_PYTHON_MATTERED.md.

**Why Jupyter Notebook?**
It keeps the code, the explanation and the result together, step by step, so the work reads
like a story.

**Why Markdown for reports?**
Plain text is easy to read, search and track over time, and it shows nicely on GitHub.

**Why Git and GitHub?**
They record every change, store the work online, and let others read and check it.

**Why Version 1 and Version 2 separately?**
Version 1 builds the index and Version 2 explains it. Keeping them apart let the index stay
frozen and stable while the analysis grew.

**Why one question per notebook?**
It stopped the notebooks from overlapping or drifting, and made the project read as a clear
chain. See PROJECT_PHILOSOPHY.md.

## 6. Limitations

**What can't this index measure?**
It measures two of Porter's four parts. It does not measure demand quality or firm competition,
and it does not include every factor that affects development. See THESIS.md, Section 10.

**Why aren't all states ranked?**
Three union territories had too little data and did not meet the 8-of-11 coverage rule, so they
were left unranked.

**Can the rankings change?**
The ranking is stable against the main technical choices, which were tested. New data or new
indicators in a later version could change it. See validation_notes.md.

## 7. Using the project

**Can researchers reuse it?**
Yes. The data is official and the code is open, so the work can be repeated and extended.

**Can students learn from it?**
Yes. It brings together data analytics, economics, public policy, research and Python in one
place.

**Can policymakers use it?**
It can show where a state's largest measured gaps are. It does not recommend schemes, so it is
a starting point, not a policy plan. Policy choices still require judgement beyond the data.
See development_priorities.md.

**Can new indicators be added?**
Yes. A later version can add indicators or new parts of the framework, as long as it keeps the
same open and documented approach. See THESIS, Section 11.

## 8. Technical

**How many notebooks are there?**
Fifteen. Notebooks 01 to 05 build the index (Version 1.0), and 06 to 15 explain it
(Version 2.0).

**Which libraries are used?**
pdfplumber for reading the PDFs, pandas for the tables, matplotlib and seaborn for the charts,
and scikit-learn for grouping.

**Which datasets are used?**
The RBI Handbook of Statistics on Indian States 2024-25, and the Ministry of MSME Annual
Report.

**How can someone reproduce the work?**
Put the source PDFs in data/raw, then run the notebooks in order from 01 to 15. Each notebook
reads what the previous one saved, and saves the outputs needed by the next notebook. See
README.md.
