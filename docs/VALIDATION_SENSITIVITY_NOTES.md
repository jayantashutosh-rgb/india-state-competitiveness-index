# Validation and Sensitivity Notes (Notebook 05)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

Notebook 04 gave one ranking of states. To make that ranking, we made a few choices.
Here we test those choices. We change one thing at a time and see if the ranking
changes. If it changes very little, we can trust the ranking.

## Why we did not do this earlier

We can only test a ranking after we have one. Notebook 04 creates the ranking. So the
testing comes after it. Before that there was nothing to test.

## Why this matters

Every ranking is based on some choices. If a small change in a choice flips the order,
the ranking is weak. This notebook shows whether the ranking is steady or not.

## What we found

The ranking stays almost the same, no matter which choice we change. The details are
below.

## The choices we tested

We tested three:

1. Unemployment. We used the average of rural and urban. What if we used only rural, or
   only urban?
2. Coverage rule. We gave a state a score only if it had at least 8 of its 11 numbers.
   What if we used 7 or 9?
3. Scale. We put all numbers on the same scale using Min-Max (0 to 1). What if we used
   another common way, called Z-score?

## What each cell does

- Setup: open the master table and bring in the scoring code from src/scoring.py. This is
  the same code Notebook 04 used, so the test scores states the same way.
- Three unemployment versions: create the ranking three times, one for rural, one for
  urban, one for the average. This shows if the unemployment choice matters.
- Rank correlation: this checks whether two rankings are almost the same or very
  different. We compare all three.
- Top and bottom check: see if the same states stay in the top 10 and bottom 10 in all
  three versions.
- Coverage rule check: create the ranking again with the rule set to 7, 8 and 9, and see
  which states come in or go out.
- Min-Max vs Z-score: score the states again with Z-score and compare with the Min-Max
  ranking.
- Summary: a short note on what all the checks say together.

## Why we reused the scoring code

The steps for putting all numbers on the same scale and averaging them already sit in
src/scoring.py. Notebook 04 and this notebook both use it. So the two do not become
different over time, and the test uses the real method.

## FAQ

### General

What is sensitivity analysis?
It means changing one thing at a time to see if the ranking changes.

Why test our own work?
A ranking is only useful if it is steady. If we do not check it, someone else might, and
they may find problems. It is better to check first.

Why is this a separate notebook?
Notebook 04 creates the ranking. This one only tests it. Keeping them apart keeps each
notebook clear.

### The unemployment check

Why test three unemployment versions?
There was no official combined number, so we made the average. This checks if that
choice changed the ranking.

What is rank correlation?
It checks whether two rankings are almost the same or very different. A number near 1
means almost the same.

What did it show?
All three versions agreed. The number was 0.99 or higher. The ranking changes very
little when we switch the unemployment number.

### The coverage check

Why change the 8 of 11 rule?
To see if the rule was too strict or too loose.

What happened?
Only two small territories changed. Ladakh came in at 7. Andaman & Nicobar went out at
9. No other state changed.

### The scale check

What is Z-score?
It is another way to put numbers on the same scale. It shows how far each state is from
the average.

Why compare it with Min-Max?
To make sure the ranking comes from the data, not from the way we scaled the numbers.
The two agreed closely, about 0.99.

### Results and next steps

Did any big state change place?
No. The top and bottom stayed the same. Only a few middle states moved a little.

Where are the results saved?
In validation_notes.md, in the results folder.

What did all this tell us?
The checks show that the choices used in Version 1.0 give almost the same ranking even
when we test other reasonable options.
