# Scenario Analysis
India State Competitiveness Index (ISCI) — Version 2.0

**Research question:** How much could a state's score change if one priority area improved?

These scenarios are simulations. They do not predict what will happen in reality. They only
show what the index would look like if the selected score improved while everything else
stayed the same.

## Method

For each state we take its main priority: the number where it is furthest below the top
group (from Notebook 11). We then raise that one number to the top group's average for that
number, and work out the state's new score and new rank. No other indicator is changed
during the simulation.

Two rules keep this simple and fair:

- The Version 1.0 normalization scale is kept fixed. Only the selected state's score is
  recalculated. Other states are unchanged.
- The same rule is used for every state: close your biggest gap. There is no arbitrary
  amount, so the states can be compared.

## What the sweep shows

Closing a state's single biggest gap raises its score by a small amount, between 0.005 and
0.08, and moves its rank by 0 to 6 places.

- Some of the biggest rank gains go to middle-ranked states, such as Tripura, Madhya
  Pradesh and Andaman & Nicobar Islands, which each rise by 6 places. Their scores sit close
  together, so a small score gain moves the rank more.
- Two strong states move to rank 1: Gujarat rises from rank 3 to 1 by closing its education
  gap, and Tamil Nadu rises from rank 2 to 1 by closing its investment gap.
- The weakest states improve but stay near the bottom. Bihar rises from 30 to 26 and
  Arunachal Pradesh from 33 to 29. Closing one gap improves their position, but it does not
  remove all of the remaining gaps.

The full sweep is saved in scenario_sweep.csv.

## Case studies

Four states, one from each kind of position.

### Bihar (Weak on both parts)

- Before: score 0.245, rank 30
- Biggest gap: factory density
- Simulation: factory density set to the top-group average (0.65).
- After: score 0.304, rank 26
- Change: score up 0.059, rank 30 to 26

### Kerala (Strong basic conditions, weaker industry)

- Before: score 0.417, rank 15
- Biggest gap: investment rate
- Simulation: investment rate set to the top-group average (0.56).
- After: score 0.458, rank 11
- Change: score up 0.042, rank 15 to 11

### Tamil Nadu (Strong on both parts)

- Before: score 0.605, rank 2
- Biggest gap: investment rate
- Simulation: investment rate set to the top-group average (0.56).
- After: score 0.613, rank 1
- Change: score up 0.009, rank 2 to 1

### Uttar Pradesh (Weak on both parts)

- Before: score 0.280, rank 27
- Biggest gap: factory density
- Simulation: factory density set to the top-group average (0.65).
- After: score 0.327, rank 24
- Change: score up 0.047, rank 27 to 24

## What we learn

- Closing one gap helps, but by a small amount. No state jumps a long way, because only one
  of eleven numbers changes.
- Some middle-ranked states gain more ranks because many states have similar scores.
- The strongest states are already near the top, so they gain little room.
- The weakest states rise a little but stay near the bottom. One gap is not enough on its
  own.

## Limits

- The simulation changes only one number at a time. In reality, improving one area may
  affect other numbers, but those links are not modelled here.
- Reaching the top-group average does not make a state one of the strongest states overall.
  It only removes its biggest measured gap.
- The scenarios use only the numbers in this index. They are a simple experiment, not a
  forecast.
- The simulation assumes that the improved indicator can change while all other indicators
  remain unchanged. In practice, this may not happen.

## Questions for the next notebook

- What are the main findings across the whole project?
- Which patterns appear again and again?

The next notebook pulls the findings together.
