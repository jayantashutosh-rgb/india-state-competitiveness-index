# Gap Analysis Notes (Notebook 11)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

This notebook measures the gaps. For every state it asks two things: how far it is below
the average, and how far it is below the strongest states. It does not say why the gaps are
there or how to close them. Those come in the next notebooks.

## Why this notebook was needed

By now we know the ranking, the groups and the types of states. But we did not know, for
each state, which numbers hold it back the most. This notebook finds that. It turns the
scores into clear gaps, so we can see where each state is short.

## What we learned

A state's weak spot depends on what we compare it with.

- Against the national average, the weak spots are spread across the basic-conditions
  numbers.
- Against the strongest states, the gap is almost always on industry.

So the two comparisons answer different questions and do not always point to the same
weakness.

## The two benchmarks

We compare each state with two things:

- The national average. This shows the state's current position: is it below or above the
  average of all states?
- The top group, the "Strong on both parts" states from Notebook 10. This is a target: how
  far is the state from the strongest group?

A positive gap means the state is below the benchmark. All the numbers are on the 0 to 1
score scale.

## What each cell does and what it found

- Setup:
  Opens the scores and the groups, and works out the two benchmarks: the national average
  and the top-group average for each number.
  Found: the top group scores higher than the average on almost every number, and much
  higher on the industry numbers.

- Gap vs the national average:
  For each state, finds the number where it is furthest below the average. This is its
  current weakness. Saves the full table.
  Found: the biggest weakness is spread across many numbers, most often manufacturing
  share, life expectancy, unemployment and road density.

- Gap vs the top group:
  For each state, finds the number where it is furthest below the top group. This is its
  development gap. Saves the full table.
  Found: for 24 of the 33 states, the biggest development gap is on factory density,
  investment or manufacturing.

- Per-state diagnostic:
  Puts together, for each state, its current weakness, its development gap and its easiest
  gap. Saves the table.
  Found: the most common easiest gap is per-capita power, but only because the top group
  itself scores low on it.

- Patterns across states:
  A short summary that ties the state-by-state gaps together.

The written report, version2/reports/gap_analysis.md, is built from these numbers.

## What we understood overall

- Against the average, a state's weak spot is often a basic-conditions number: 23 of 33
  states.
- Against the top group, the weak spot flips to industry: 26 of 33 states.
- Most states already match or beat the top group on unemployment, road density, life
  expectancy and schooling. The fewest match it on the industry numbers.
- So the path to the top runs mainly through industry.

## FAQ

### General

What is a gap?
The distance between a state's score and a benchmark. A positive gap means the state is
below the benchmark.

Why use two benchmarks?
They answer different questions. The average shows where a state stands now. The top group
shows how far it is from the best.

Does this notebook say how to fix the gaps?
No. It only measures them. Fixing them is the job of the policy notebook.

### Weakness and development gap

What is the difference between them?
The current weakness is the number where a state is furthest below the average. The
development gap is the number where it is furthest below the top group. They are often
different.

Why do the two often disagree?
Because the average and the top group are set at different levels. A state can be above the
average on a number but still far below the top group on it.

### The easiest gap

What is the easiest gap?
Among the numbers where a state is below the top group, it is the one with the smallest gap.

Why is per-capita power the most common easiest gap?
Because the top group itself scores low on per-capita power (0.12). The gap is small because
the target is low, not because power is easy to improve. A small gap only means the state is
already close to the benchmark on that number.

### Next

What happens after this notebook?
Notebook 12 uses these gaps to suggest what different states could focus on.
