# State Profiles Notes (Notebook 07)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

This notebook makes one short profile for every ranked state. A profile is a small report
that shows the state's rank, its scores, its strongest and weakest indicators, and how it
compares with the national average and the top state. It only uses the numbers. It does
not explain why a state is high or low. That explanation starts in Notebook 08.

In the project's flow, this is the state diagnosis step: it works out how each state
performs. The word "profile" is kept because it is the common term in government and
research reports.

## Why it is a separate notebook

Notebook 06 looked at the data as a whole. This notebook looks at one state at a time. It
turns the numbers into a readable card for each state, which the later notebooks build on.

## Why it stays data only

The rule for Version 2.0 is that describing and explaining are kept apart. Here we only
describe each state. The "why", the economics, and the policy advice come later, so the
profiles stay simple and hard to argue with.

## Where the profiles are saved

Each state gets its own Markdown file in `version2/reports/state_profiles/`, for example
`gujarat.md`. Separate files are easy to read on GitHub, easy to update one at a time,
and easy to turn into a website or PDF later. The Version 1.0 files are never changed.

## What each part does

- Setup:
  Opens the Version 1.0 files, makes the profiles folder, and works out the national
  average and the top-ranked state.

- Profile data:
  A function that gathers all the numbers for one state: its rank and scores, its two
  dimension scores, its top and bottom indicators, and how far it sits from the national
  average and the top state.

- Build one profile:
  A function that puts those numbers into a fixed template and returns the Markdown text.
  The observations are plain facts, and the questions are left open.

- Write all profiles:
  A loop that saves one file per ranked state.

## What is in each profile

- Rank, overall score, and coverage.
- A quick summary in one line.
- Factor Conditions: strongest and weakest indicators.
- Related & Supporting Industries: strongest and weakest indicators.
- Top 5 and bottom 5 indicators.
- Comparison with the national average.
- Comparison with the top-ranked state.
- Data-based observations.
- Questions suggested by the data for later analysis.

Every profile follows exactly the same format, so states can be compared easily.

## FAQ

### General

What is a state profile?
A short card that shows how one state does on the index, using only its numbers.

Why one file per state?
It is easier to read, update and share than one very long file with every state in it.

Does this notebook explain why a state ranks where it does?
No. It only describes the state. The reasons come in Notebook 08 and later.

Which states get a profile?
The 33 ranked states. The three union territories with too little data are left out.

### The content

What is a dimension score?
The average of the indicators in one group. Factor Conditions is one group, Related &
Supporting Industries is the other.

What does "comparison with the national average" mean?
For each indicator, it checks whether the state is above or below the average of all
states.

Why are the questions left open?
Because answering them needs interpretation, and that belongs in the later notebooks.
Here we only raise the questions the data points to.

Why are there no charts in the profiles?
The profiles are meant to be short and easy to read. Charts are already in Notebook 06,
and can be added later if needed.

### Data

Why are the profiles based on Version 1.0 results?
Version 2.0 does not rebuild the index. It reads the final outputs from Version 1.0 and
uses them to create the state profiles. This keeps the analysis separate from the index
construction.

### Next

What happens after this notebook?
Notebook 08 is the first interpretation notebook. It uses Michael Porter's Diamond
framework to explain the patterns seen in the state profiles.
