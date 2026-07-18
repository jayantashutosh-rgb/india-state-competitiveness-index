# Index Construction Notes (Notebook 04)
India State Competitiveness Index (ISCI)

---

## What happens here

By now the data is clean and ready in one table, made in Notebook 03. Here we use that
table to give every state one final score and put the states in order, from strongest to
weakest.

Each state has several indicators such as education, health, employment, roads,
industry and banking. This notebook combines them into one competitiveness score and
produces the final ranking.

## What is different about this notebook

The earlier notebooks collected and cleaned the data. They read the PDFs, pulled out
tables, and worked out new numbers. None of them gave a final score.

This notebook calculates the final score and produces the state ranking. It does not
change any original number. It only takes the ready numbers and joins them into one
score.

## Why this was not done in an earlier notebook

Collecting data and scoring data are two different jobs. If we mixed them, one notebook
would become very long and hard to read. Keeping the scoring on its own also lets us
change the scoring method later without touching the data work.

## How the score is calculated

The process is straightforward:

1. The numbers are in different units. Some are percentages, some are counts, some are
   ratios. You cannot add them as they are. So we change each one to a value between 0
   and 1. Now they are all on the same scale.
2. For most numbers, higher is better. But for two of them, unemployment and power loss,
   higher is worse. We flip those two, so that a high score always means good.
3. For each state, we take the average of its numbers. Every number counts the same.
4. A state gets a final score only if it has at least 8 of the 11 numbers. If too many
   are missing, we do not score it.
5. We also make two group scores, only to understand each state better. These are not
   part of the final score.

## What each cell does and why

- Setup: load the tools and open the ready table from Notebook 03.
- Make the working table: join rural and urban unemployment into one number, then keep
  the 11 numbers we need, in their two groups.
- Mark direction: note the two numbers where higher is worse, unemployment and power
  loss.
- Scale the numbers: change every number to sit between 0 and 1, and flip the two marked
  ones.
- Check coverage: for each state, count how many of the 11 numbers it has, and mark
  which states have at least 8.
- Save the scaled numbers: write them to indicator_scores.csv in the results folder.
- Group scores: average the numbers inside each group and save them as
  dimension_scores.csv.
- Final score and rank: average each state's numbers, put the states in order, add the
  coverage columns, and save as competitiveness_index.csv.

The file validation_notes.md is written by hand, not by the notebook.

## What this notebook produces

The notebook creates the final competitiveness scores and state rankings.

It also records how many indicators were available for each state, so the coverage of
every score is clear.

The complete ranking is saved in competitiveness_index.csv.

## Frequently Asked Questions

Why turn every number into a value between 0 and 1?
Because the numbers use different units. A percentage and a count cannot be added
directly. Once they all sit between 0 and 1, we can compare and average them fairly.

Why flip unemployment and power loss?
For these two, a big number is bad. If we do not flip them, a weak state would look
strong. After flipping, a high score always means good, for every number.

Where do the smallest and largest values come from?
Only from these 36 states. So a score of 1 means the best among these states, not a
perfect target.

Why does every number count the same?
Equal weights avoid making assumptions about the relative importance of the indicators.
The source does not provide any basis for assigning different weights, so every
indicator is treated equally.

Why average only the numbers a state has?
A state should not lose marks just because one number is missing. As long as it has
enough of them, we average what it has.

Why the rule of 8 out of 11?
If a state has too few numbers, its score is not trustworthy. The rule keeps such states
out of the ranking, but we still show how much data they had.

What are the two group scores for?
They help explain a state's rank. They show whether a state is doing well because of its
basic conditions or because of its industries. They do not change the final score.

Which states get no score?
Three small union territories with too little data: Dadra & Nagar Haveli and Daman &
Diu, Lakshadweep, and Ladakh.

Why does Chandigarh use only its city (urban) unemployment?
The source reports only the urban number for Chandigarh. Since Chandigarh is almost
fully a city, that number is used as it is. No value is estimated or filled in.

Why are all the final scores close to each other?
Most states are strong in some areas and weaker in others. When the indicators are
averaged, the final scores become closer together, so the ranking is usually more
useful than the score itself.

Does the unemployment unit change the result?
No. Unemployment is reported per thousand people, not as a percentage. Scaling to 0 and
1 removes the effect of the unit, so the scores and the ranking stay the same.

What files does this notebook make?
Four files in the results folder: indicator_scores.csv, dimension_scores.csv,
competitiveness_index.csv, and validation_notes.md.

What happens after this notebook?
Notebook 05 tests how sensitive the ranking is to different assumptions, such as the
choice of unemployment measure and the coverage rule.
