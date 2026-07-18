# Exploratory Data Analysis Notes (Notebook 06)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

Before we explain the ranking, we look at the data itself. This notebook makes charts to
describe the numbers: how they are spread out, what is missing, and how they relate to
each other. No new data and no new scores are made here. It only reads the Version 1.0
files and draws pictures from them. It does not explain why states rank where they do;
that comes in the later notebooks.

## Why it is a separate notebook

Notebooks 01 to 05 built the index and tested it. This is the first notebook of Version
2.0. Version 2.0 is about understanding and explaining the index. So we start by getting
to know the data.

## Why we did not do this earlier

We could have looked at the data sooner. But Version 1.0 had one job: build the index
from start to finish. Now that the index is done and frozen, Version 2.0 begins by
describing the same data more closely.

## Where the charts are saved

Every chart is saved as a picture in `version2/figures/eda/`. The Version 1.0 files are
never changed.

## What each part does

- Setup:
  Opens the Version 1.0 files (the raw numbers, the scaled scores, the dimension scores
  and the final ranking). Nothing is changed.

- Summary statistics:
  Shows a table with the average, the spread and the range of each indicator.
  The indicators use very different units.

- Missing values:
  Shows how much data is missing, by indicator and by state.
  Most gaps are in life expectancy and in a few small union territories.

- Indicator distributions:
  Shows a histogram for each indicator.
  Many indicators are lopsided rather than evenly spread.

- Boxplots and outliers:
  Shows the middle range of each indicator and marks states that sit far outside it.
  Only a few states stand out as outliers.

- Correlation:
  Shows how strongly different indicators move together.
  Some indicators have a strong relationship, while others are weak or negative. The
  reasons are explored in later notebooks.

- Key relationships:
  Shows scatter plots for a few pairs of indicators.
  The dots follow a clear line for some pairs and not for others.

- Score distributions:
  Shows the shape of the final score and the two dimension scores.
  The final scores are close together, and the two dimensions have different spreads.

- Top 10 vs bottom 10:
  Shows the average of each indicator for the strongest and weakest states.
  It highlights where the largest differences appear. These differences are analysed in
  the following notebooks.

- Summary of findings:
  A short list that puts together what the charts show.

## FAQ

### General

What is EDA?
EDA means exploratory data analysis. It is the step where we look at the data with simple
charts before we try to explain anything.

Why look at the data if the index is already built?
Charts show patterns that a table hides. They prepare the ground for the later notebooks,
which explain the results.

Does this notebook change the index?
No. It only reads the Version 1.0 files and draws charts. Nothing is changed.

Why does this notebook not explain why a state is high or low?
That is the purpose of the later notebooks. This notebook only explores the data and
shows patterns. The interpretation comes afterwards.

### The charts

Why do we scale the numbers before comparing them?
The indicators use different units. Power is in thousands, roads in hundreds, investment
near one. Putting them on the same 0 to 1 scale lets us compare them fairly.

What does skew mean?
Skew tells us if the values are lopsided. A high skew means a few states have very large
values and most states are low.

What is an outlier?
A value that sits far away from the rest. For example, a small union territory can have
very high power use per person.

What does correlation show?
Whether two indicators move together. Near +1 they rise together, near -1 they move
opposite ways, and near 0 they have little link.

Why does road density behave differently from the other indicators?
Road density follows a different pattern from several other indicators. The reason is
examined in the later notebooks.

### Results

What do the charts show overall?
Some indicators differ a lot between states, some are lopsided, and some are missing for
small territories. What these differences mean is covered in the later notebooks.

Why are the final scores so close together?
No state is strong on every indicator, so averaging brings the scores near the middle.

### Next

What happens after this notebook?
Notebook 07 studies each state one by one: its rank, its strengths, its weaknesses, and
where it stands compared with the average and the top state.
