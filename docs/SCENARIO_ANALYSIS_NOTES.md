# Scenario Analysis Notes (Notebook 13)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

This notebook runs a simple "what if" test. For each state it asks: if the state improved
its main priority, how much would its score and rank change? It is a simulation. It does not
predict the future. It only shows what the index would look like if one number went up while
everything else stayed the same.

## Why this notebook was needed

Notebook 11 found each state's biggest gap. Notebook 12 turned that gap into a priority. But
neither one showed what would happen if a state actually closed that gap. This notebook does
that. It completes the chain: measure the gap, identify the priority, then test what happens
if that gap is closed.

## What we learned

Closing one gap helps, but only a little. Scores go up by a small amount, and ranks move by
0 to 6 places. No state jumps a long way, because only one number out of eleven changes. The
weakest states improve, but they remain among the lowest-ranked states because they still
have several remaining gaps.

## The rule we use

We keep it simple and the same for every state:

- Take the state's main priority (its biggest gap to the top group).
- Raise that one number to the top group's average for that number.
- Keep the Version 1.0 scale fixed, and leave every other state and every other number
  unchanged.
- Work out the new score and the new rank.

Because the rule is the same for all states (close your biggest gap), the results can be
compared. There is no made-up amount like "improve by 0.2".

## What each cell does and what it found

- Setup:
  Opens the scores, the ranking and the groups. Works out each state's main priority and the
  top group's average for each number.

- Simulate closing the biggest gap:
  For every state, raises its main-priority number to the top-group average and finds the
  new score and rank. Saves the full table.
  Found: ranks move by 0 to 6 places. Some middle-ranked states move the most, because their
  scores sit close together.

- Case studies:
  Shows four states in detail, one from each kind of position: Bihar, Kerala, Tamil Nadu and
  Uttar Pradesh.
  Found: Tamil Nadu reaches rank 1, Kerala rises four places, and Bihar and Uttar Pradesh
  rise a little but stay near the bottom.

The written report, version2/reports/scenario_analysis.md, is built from these numbers.

## What we understood overall

- One gap is not enough on its own. A weak state stays weak after closing only its biggest
  gap. Most states need improvements in more than one area to move much further up the
  ranking.
- Middle-ranked states can move the most places, because many states have similar scores.
- The strongest states are already near the top, so they gain little room.

## FAQ

### General

What is a simulation here?
A "what if" test on the numbers. We change one score and see what the index would look like.
It is not a prediction.

Does this notebook change the index?
No. The real index stays fixed. We only recalculate one state's score while leaving every
other state unchanged.

Why keep the scale fixed?
So that only the chosen state moves. If we re-scaled everything, other states would move too,
and the "what if" would no longer be about one state.

### The rule

Why raise the number to the top-group average, and not by a fixed amount?
A fixed amount, like "improve by 0.2", has no clear meaning. Raising the number to the top
group's level has a clear meaning: the state closes its biggest gap. It also uses the same
rule for every state.

Why only one number at a time?
To keep the test simple and clear. In real life, indicators can influence one another, but
those relationships are outside the scope of this simulation.

### The results

Why do some middle states gain the most ranks?
Because many states have similar scores in the middle. A small rise in score can pass several
of them.

Why do weak states stay near the bottom?
They have more than one large gap. Closing only the biggest one is not enough to lift them
far.

### Next

What happens after this notebook?
Notebook 14 pulls together the main findings from the whole project.
