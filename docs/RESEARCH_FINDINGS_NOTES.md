# Research Findings Notes (Notebook 14)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

This notebook gathers the main findings from the whole project into one place. It does not
run any new analysis. It opens the saved outputs, prints the headline numbers, and checks
that they match what the earlier notebooks found.

## Why this notebook was needed

By now the project has many notebooks and many result files. A reader needs a single, short
place that says what it all adds up to. This notebook is that place. It also proves the
findings, because it reads them straight from the saved files.

## What we learned

Nothing new is learned here. The notebook simply confirms and collects what Notebooks 06 to
13 already showed:

- States differ in overall competitiveness (Notebook 07).
- States fall into three groups (Notebook 10).
- Basic conditions shape a state's position against the average (Notebook 11).
- Industry sets the distance to the strongest states (Notebooks 11 and 12).
- Closing one gap helps only a little (Notebook 13).

## How it works

The notebook is read-only. It loads the final ranking, the groups, the two gap tables, the
priorities and the scenario sweep. Then it prints the key numbers for each, so they can be
checked against the reports. No number is recalculated beyond reading and counting the saved
results.

## What each cell does

- Setup: opens all the saved output files.
- Ranking recap: prints the number of states and the highest and lowest scores.
- Groups recap: prints how many states are in each of the three groups.
- Gaps recap: prints how many states have their biggest gap in basic conditions and how many
  in industry, against both benchmarks.
- Priorities recap: prints how many states have an industry-related main priority.
- Scenarios recap: prints the range of score gains and rank moves.

The written report, version2/reports/research_findings.md, is built from these numbers, and
every finding names the notebook it came from.

## FAQ

Does this notebook add new findings?
No. It only gathers and confirms findings from the earlier notebooks.

Why print the numbers again?
So a reader can check that the summary matches the saved results, without re-running the
whole project.

Why does every finding name a source notebook?
So the reader can trace each point back to where it was measured. It also shows that this
notebook only summarizes, and does not invent anything.

## Next

What happens after this notebook?
Notebook 15 prepares the final report and a short executive summary.
