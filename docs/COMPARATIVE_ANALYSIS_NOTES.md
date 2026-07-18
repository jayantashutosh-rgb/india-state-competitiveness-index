# Comparative Analysis Notes (Notebook 09)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

This notebook compares groups of states, not one state at a time. Notebook 07 looked at
each state on its own. This notebook puts states into groups and asks how the groups are
different. It uses only the numbers from the index. It shows the numbers first, then says
what we can learn from them.

## Why it is a separate notebook

Looking at one state and comparing many states are two different jobs. Notebook 07 handled
each state on its own. This notebook is only about comparing. Keeping them apart makes each
notebook easier to follow.

## Why this could not be done earlier

To compare states fairly, we first needed each state's scores. Those came from the index in
Version 1.0. We also wanted to understand each state on its own, which Notebook 07 did.
Only after that does comparing groups make sense. So this step comes here.

## Why this notebook matters

A single ranking tells you the order. Comparing groups tells you the patterns. It shows
whether the strong states share something, and whether the weak states share a problem.
These patterns are the start of the story that the later notebooks build on.

## How the groups are made

We put states into simple groups so we can compare them:

- Region: North, South, East, West, Central, North-East, and Islands. These are common
  geographic groups. They are used only for comparing and are not part of the index.
- Coastal or inland: whether a state touches the sea. This is a plain map fact.
- Large or small: we split states by population at the middle value. Half are large and
  half are small. This is only for comparing and does not change the index.

## What each cell does

- Setup:
  Opens the Version 1.0 results and puts each state into its groups (region, coast, size).
  Nothing is changed.

- Top 10 vs bottom 10:
  Takes the average of each number for the top ten states and the bottom ten states, and
  finds the biggest gaps between them.

- Region comparison:
  Takes the average score of each region. Small regions are marked, because a group with
  very few states is easy to move up or down.

- Coastal vs inland:
  Compares the coastal states with the inland states, and shows which numbers differ most.

- Large vs small:
  Compares large and small states in the same way.

- Case studies:
  Compares five chosen pairs of states, one pair at a time, and shows the numbers where
  each state leads.

The written report, version2/reports/comparative_analysis.md, is built from what these
cells produce.

## About the questions at the end

The report ends with a few questions for the next notebook. These are not answers. They
are questions the comparisons point to, such as whether states can be grouped into types
on their own. The next notebook works on them. Leaving them open, instead of guessing,
keeps the work honest.

## FAQ

### General

What does this notebook compare?
Groups of states: the top ten against the bottom ten, region against region, coastal
against inland, and large against small. It also looks at five pairs of states.

Does it give opinions or advice?
No. It only shows the numbers and says what we can learn from them. Advice comes in the
later policy notebook.

Does it change the index?
No. It only reads the Version 1.0 results.

### The groups

Are the regions official data?
No. They are common geographic groups, used only for comparing. They are not part of the
index.

How are large and small states decided?
By population, split at the middle value. Half the states are large and half are small.
This is only for comparing.

Why are some region averages marked as weak?
Some regions have very few states. West has 3, Central has 2, and Islands has just 1. A
small group can move up or down easily, so its average is less reliable.

### The findings

What is the main pattern?
In almost every comparison, the biggest differences come from factory density,
manufacturing, investment and MSMEs. These separate states more than most of the
basic-condition numbers.

Why is road density different?
Road density is counted per person. Small states, with fewer people, can score higher on
it. So it often goes the other way from the industry numbers.

### Next

What happens after this notebook?
Notebook 10 groups the states into types using their scores, to see which states are
alike.
