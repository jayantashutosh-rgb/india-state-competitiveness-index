# Lessons Learned

This is a look back at the project. Every lesson below comes from something that actually
happened while building the India State Competitiveness Index. These are not general sayings.
They are the specific things this project taught us.

## What we learned about India

- Industry, more than basic living conditions, separates the strongest states from the rest.
  Factories, manufacturing, investment and small businesses are where the top states pull
  ahead.
- The western and southern states lead. Gujarat, Goa, Tamil Nadu and others sit at the top.
  The north-eastern states, and the large northern states Bihar and Uttar Pradesh, sit near
  the bottom.
- Some states are strong on basic conditions but weak on industry, such as Kerala and Delhi.
  Good schooling and health do not automatically bring a strong industrial base.
- In small states, numbers measured per person, like power or roads, can look very high. Size
  changes how a number should be read.

## What we learned about government data

- Official data is spread out. It sits in long PDF reports, in different units and different
  years. Bringing it together is most of the work.
- Some data does not match the state list. Telephone data is reported by telecom circle, not
  by state, so it could not be used.
- Some figures are missing. Gujarat's latest income and GVA numbers were not published yet,
  which almost pushed a major state out of the index until we handled it.
- Not every file is useful. One spreadsheet that looked like GDP data turned out to be a list
  of notices, not data at all.
- Units must be checked. Unemployment looked impossibly high until we saw it was reported per
  thousand people, not as a percentage.

## What we learned about Porter's theory

- A framework guides the work, but the data decides what can be measured. Only two of
  Porter's four parts had reliable state-level official data.
- It is better to measure two parts well than to guess the other two. Demand and firm
  competition were left out and clearly marked as limits, instead of being filled in.

## What we learned about Python

- Code that refuses to guess is safer than code that always produces a number. When a table
  could not be read cleanly, stopping was the right choice.
- Automation made the work repeatable and made future updates easy.
- The full story is in WHY_PYTHON_MATTERED.md.

## What we learned about research

- Keep evidence and interpretation apart. First show the numbers, then say what they may
  mean. This kept the claims honest.
- Two numbers moving together does not prove one causes the other. We said this often, on
  purpose.
- Give each notebook one question. This stopped the notebooks from repeating each other.

## What we learned about documentation

- Plain, simple language makes a technical project readable by anyone.
- Writing down each decision, and why it was made, made the choices easy to trace later.
- A steady structure across all the notes made the whole repository feel like one project.

## What we learned about reproducible science

- Freezing Version 1.0 and building Version 2.0 on top kept the index stable while the
  analysis grew.
- Saving the results of each step, as CSV files, let later notebooks build on earlier ones
  without redoing the work.
- Keeping the scoring code in one shared file meant the index and the tests always used the
  same method.

## What surprised us

- Clustering revealed a clear middle group of states that are strong on basic conditions but
  weak on industry. This pattern was not obvious before.
- Gujarat, a top-five economy, almost dropped out of the index because its newest figures
  were unpublished. A small choice about which year to use had a big effect.
- The "easiest gap" was often per-capita power, but only because the top group itself scores
  low on it. A small gap did not mean easy improvement.
- One early claim, that life expectancy varied little between states, turned out to be false
  when we checked the numbers. Checking beats assuming.

## What we would do differently next time

- Decide how to handle missing recent years at the very start, before building features.
- Save the group labels from the clustering step earlier, so later notebooks can reuse them.
- Look for demand and firm-competition data sooner, to see how far the framework can reach.
- Separate related indicators, like power supply and power losses, from the beginning, to
  avoid confusion later.

## In one line

The biggest lesson was simple: careful data work, honest limits and clear writing matter more
than clever analysis.
