# Porter's Diamond Notes (Notebook 08)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

This notebook uses Michael Porter's Diamond to understand why some states score higher
than others. Notebook 07 told us how each state does. This notebook asks the next
question: why? It reads the Version 1.0 results and tries to make sense of them, one part
of the Diamond at a time. First we show the numbers. After that we say what those numbers
may mean. When a line is our own thinking and not just a number, we say so.

## Why it is a separate notebook

Showing the numbers and explaining them are two different jobs. Notebook 06 looked at the
data. Notebook 07 described each state. Neither one gave reasons. This notebook is the
first one that gives reasons. Keeping it on its own makes it clear where the plain numbers
end and our thinking starts.

## Why this could not be done earlier

You can only explain a result after you have it, and after you have described it. The
index was built in Version 1.0. Each state was described in Notebook 07. Only then can we
step back and look at the full picture through Porter's Diamond. So the explanation comes
here, not before.

## Why this notebook matters

This notebook is where we start understanding the ranking instead of only looking at it. A
ranking on its own just gives the order. This notebook tells us what is behind the order.
It shows which parts of the Diamond are strong, which are weak, and what that may mean.
This is the part that turns a data project into real thinking.

## What each cell does and why

- Setup:
  Opens the Version 1.0 results and the income numbers used only to describe demand.
  Nothing is changed.

- Factor Conditions numbers:
  Works out which states are strongest and weakest on the basic inputs. It also shows
  which of the seven numbers states score high and low on, and how closely this part moves
  with the final score. These numbers feed the Factor Conditions part of the report.

- Related & Supporting Industries numbers:
  The same for the four industry numbers. It also checks how spread out these scores are,
  which turns out to matter a lot.

- Demand numbers:
  Loads the two income numbers, the size of the economy and income per person, and checks
  how they line up with the ranking. We do not have direct data for demand, so these
  income numbers only give a rough idea. They are not part of the index.

- Firm competition note:
  A short note. This part has no good official data, so we write down that it is missing
  instead of guessing.

- Overall picture numbers:
  Checks how the two measured parts move together, and lists the states that are strong or
  weak on both. This feeds the final summary.

The written report, version2/reports/porter_diamond_analysis.md, is built from the numbers
these cells produce.

## About the open questions

Each part of the report ends with a few open questions. These are not answers. They are
questions the numbers point to. We keep them for the notebooks that come next. For
example, "why do Bihar and Uttar Pradesh score low even though they are so big?" is not
answered here. We carry it forward to the gap and policy notebooks. Leaving these
questions open, instead of guessing, keeps the work honest.

## FAQ

### General

What is Porter's Diamond?
A simple idea about why some places are better for business. It looks at four things: the
basic inputs a place has, the local demand, the supporting industries, and how firms
compete.

Why explain the index at all?
A rank only gives the order. The reasons behind the order are what make the project
useful.

Does this notebook change the index?
No. It only reads the Version 1.0 results and the income numbers, and writes an
explanation.

### The numbers and what they may mean

What is the difference between the two?
The numbers are the plain facts, like which states score highest. What they may mean is
our own reading of those facts. In the report we show the numbers first. After that we say
what they may mean.

Why do you keep saying "moving together does not prove cause"?
Two numbers can go up and down together without one causing the other. Saying they move
together is fair. Saying one causes the other would need more proof.

What does a number like 0.83 mean?
It shows how closely two things move together, from 0 to 1. Near 1 means they almost
always go up and down together. Near 0 means there is little link.

### The four parts

Why are only two parts fully measured?
The index measures the basic inputs (Factor Conditions) and the supporting industries
(Related & Supporting Industries). There is good official state-level data for these.

Why is demand only a rough idea?
There is no direct state-level number for local demand in the data. So we use income
numbers, the size of the economy and income per person, to get a rough idea. They only
sit close to the real thing.

Why is firm competition left out?
There is no good official state-level data for it in Version 2.0. Instead of guessing, we
write it down as missing and note one number that could be used later.

### What the numbers mean

What does "power per person" mean?
How much electricity is available for each person in the state.

What does "power lost on the way" mean?
Electricity that is lost between the power plant and homes. Less loss is better.

What does "road length per person" mean?
The length of roads compared with the number of people.

What is the credit-to-deposit ratio?
How much banks lend out compared with the money people keep with them. A higher number
means more of the savings are being lent for use in the state.

What do "factory density" and "MSME density" mean?
The number of factories, and the number of small and medium businesses, compared with the
number of people. Comparing "per person" makes big and small states fair to compare.

### Results

What is the main thing we found?
The ranking is shaped mostly by industry. The industry part moves more closely with the
final score, and it spreads states out more than the basic-inputs part.

Which states are strong all round?
Five states are strong on both measured parts: Goa, Puducherry, Punjab, Tamil Nadu and
Telangana.

### Next

What happens after this notebook?
Notebook 09 puts two states side by side, one pair at a time, to see what makes the gap
between them.
