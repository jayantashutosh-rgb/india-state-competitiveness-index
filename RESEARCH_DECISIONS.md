# Research Decisions

This document is not about explaining what was done. It explains why each important design
decision was made. Every decision is based on what actually happened during the project. The
reasons are not invented after the fact.

Research is a series of decisions. Every project could be built in many different ways. This
document explains why each important decision was made here, what other options were
considered, and what trade-offs were accepted.

Where another method could also work, we say so. No method here is claimed to be the best for
every project. Each choice has trade-offs.

## 1. Why Michael Porter's Diamond?

Porter's Diamond is a well-known idea about why some places are better for business. It gives
a clear structure: a few parts that together shape competitiveness.

We did not use GDP or per-capita income, because those measure the size or wealth of an
economy, not what makes it competitive. We did not use the Human Development Index, because it
measures development, not business strength. We did not use Ease of Doing Business, because it
is based on surveys, not on the official state data we had.

Porter fits because its parts can be linked to official indicators. Its limit is that not
every part can be measured with the data available.

Porter was chosen before the data collection started. The data was selected to match the
framework, not the other way around.

## 2. Why only two of the four parts?

Porter's Diamond has four parts. We measured two: Factor Conditions and Related & Supporting
Industries. These had reliable official data for every state.

The other two, Demand Conditions and Firm Strategy, did not have clean state-level official
data. Rather than guess them, we left them out and said so clearly. Measuring two parts well
is better than making up the other two.

## 3. Why only official government data?

Official data can be checked by anyone, is free to use, and lets others repeat the work. This
keeps the project transparent and reproducible.

The trade-off is that official data has gaps, comes in different units, and is sometimes a
year or two behind. We accepted this to keep the project open and honest.

Official data may not always be perfect, but it is transparent. Anyone can download the same
reports and repeat the work.

## 4. Why only 11 indicators?

The number 11 is not special. These were the indicators that were reliable, available for
most states, and comparable across states. Some possible indicators were dropped because they
did not cover all states or did not match the state list.

## 5. Why equal weights?

We gave every indicator the same weight. The data gives no reason to say one indicator matters
more than another, so equal weights are the most honest and easiest to explain.

Other methods exist. Expert weights depend on opinion. PCA (a data-driven method) is hard to
explain and can be unstable with only 33 states. AHP needs expert comparisons. All of these
add assumptions, so we did not use them. Equal weights can be argued against, but they are
clear, and a reader can check them at once.

Equal weights are a modelling choice. They are not a statement that every indicator is equally
important in real life.

## 6. Why Min-Max normalization?

Min-Max puts every indicator on a 0 to 1 scale and keeps the shape of the data. It is easy to
explain: 1 is the best among these states, 0 the lowest.

Z-score also works, but it is harder to read. Ranking and percentiles lose the size of the
differences between states. We chose Min-Max for clarity, and we tested Z-score as well. The
ranking barely changed, so the choice does not drive the result.

Min-Max changes the scale of the numbers, but it does not change the original data.

## 7. Why an average and not a weighted average?

Because we chose equal weights, the score is a simple average of a state's indicators. A
weighted average would need weights, and we had no fair basis to set them.

## 8. Why the 8-of-11 coverage rule?

A score built from too few indicators is not trustworthy. We required at least 8 of the 11.

Two other options were possible. Complete-case analysis would keep only states with all 11,
which would drop several states. Imputation would fill missing values with guesses, which
breaks our no-guessing rule. The 8-of-11 rule is a middle path. We tested 7 and 9 as well, and
the main ranking hardly moved.

## 9. Why a sensitivity analysis?

A single ranking can hide the effect of the choices behind it. We tested the ranking against
three choices: the unemployment measure, the coverage rule and the scaling method. The order
barely changed, so the ranking is stable. Without this test, we could not say that.

## 10. Why clustering?

Clustering was not used to look advanced. It answered a real question: do the states form
natural types? The answer was yes, and it revealed a middle group that was not obvious before.

The clusters were used to describe the data, not to label states as good or bad.

## 11. Why K-Means?

K-Means is simple and standard, and it worked well on the two dimension scores. Hierarchical
clustering would also work and gives a tree of groups. DBSCAN is meant for finding odd shapes
and outliers, which did not fit 33 states in a simple two-number space. K-Means was the
clearest choice here.

## 12. Why three clusters?

The separation score was highest at two clusters, but two clusters only split states into
strong and weak. Three clusters scored almost as well and showed a clear middle type. We chose
three because it is more useful to understand, not only because of the score.

## 13. Why gap analysis?

Before suggesting where a state should focus, we had to measure where it is behind. Gap
analysis does this, against the national average and against the top group. It is the base for
the priorities.

## 14. Why priorities and not policy recommendations?

This is a firm boundary of the project. The data can show where a state is behind. It cannot
show which government scheme would fix it. So we give priority areas, not policy
prescriptions. Giving a specific scheme would go beyond what the data can support.

Choosing a policy needs many things that are outside this project, such as budgets, politics,
institutions and local conditions.

## 15. Why scenario analysis and not prediction?

The data can show what the index would look like if a state improved one number. It cannot
predict what will really happen, because it has no model of cause and effect. So we call these
scenarios, not forecasts, and we say so on every page.

The simulations answer "What could happen inside the index?" They do not answer "What will
happen in the real world?"

## 16. Why simulations at this simple level?

We changed one indicator at a time and kept the scale fixed, so only the chosen state moves.
This is easy to follow and hard to misread. A more complex model would need assumptions we
could not support with this data.

## 17. Why Python?

For the full reasons, see WHY_PYTHON_MATTERED.md. In short, Python made a locked PDF of
official data usable, removed hand-copying, and made every step repeatable and checkable.

## 18. Why Jupyter Notebook?

Jupyter keeps the code, the explanation and the result together, step by step. A reader can
follow the work like a story, which suits a research project meant to be understood, not just
run.

## 19. Why Markdown reports?

Markdown is plain text. It is easy to read, easy to search, easy to track over time, and shows
nicely on GitHub. A Word file would be harder to version and share.

## 20. Why Git and GitHub?

Git records every change, so the growth of the project can be seen. GitHub stores it online, so
others can read it, check it and suggest improvements, and the dates show when each part was
done.

## 21. Why Version 1.0 and Version 2.0 separately?

Version 1.0 builds the index. Version 2.0 explains it. Keeping them apart meant the index could
be frozen and stable while the analysis grew on top of it. If we had changed the index during
the analysis, the results would keep shifting and could not be trusted.

This separation also reduced the risk of accidentally changing the index while the analysis
was still growing.

## 22. Why one research question per notebook?

Each notebook answers one question. This stopped the notebooks from overlapping or drifting.
It also made the project read like a clear chain: explore, describe, interpret, compare,
group, measure gaps, set priorities, test scenarios. This was one of the strongest design
choices.

One notebook answered one question. One answer naturally led to the next question. This kept
the project organised and stopped the analysis from becoming confusing.

## 23. Why freeze notebooks after they are done?

Once a stage was checked and correct, it was treated as final. Later notebooks then build on a
stable base. If earlier notebooks kept changing, every later result would have to be redone.

## 24. Why separate the reports from the notebooks?

The notebooks are the working code. The reports are the clean, readable output for people who
will not run the code. Keeping them apart means a reader can read the findings without reading
the code, and a coder can read the code without wading through prose.

## 25. Lessons from these decisions

Most of these choices share one idea: prefer the simple, honest option that a reader can
check, and be open about its limits.

If the project were started again today, most decisions would stay the same: official data,
equal weights, Min-Max, the coverage rule, the clean boundaries between measuring, prioritising
and simulating. A few things would change from the start: how missing recent years are
handled, saving the group labels earlier, and looking for demand and firm-competition data
sooner.

## Decisions we changed during the project

Some decisions were revised as the work went on. This is normal, and it is recorded here so
the project's growth is clear.

- Power was split into two areas, power supply and power losses, after one state showed the
  same area as both its biggest and its smallest gap.
- The cluster labels were saved to a file, so later notebooks could reuse them instead of
  redoing the grouping.
- The gap work separated two ideas that were first mixed: the current weakness (against the
  national average) and the development gap (against the top group).
- The scenario method was set to "close the biggest gap to the top group", after a fixed
  amount like "plus 0.2" was found to have no clear meaning.
- The reference year for income and GVA was fixed at 2022-23, after the newest year was found
  to be missing for Gujarat.

## Summary table

| Decision | Chosen | Main reason | Alternative considered | Again? |
|----------|--------|-------------|------------------------|--------|
| Framework | Porter's Diamond | Structure tied to official data | GDP, HDI, Ease of Doing Business | Yes |
| Parts measured | 2 of 4 | Only these had reliable state data | All four | Maybe, if better data becomes available |
| Data | Official government | Open and reproducible | Private or survey data | Yes |
| Weights | Equal | Transparent, no hidden assumption | Expert weights, PCA, AHP | Yes |
| Normalization | Min-Max | Easy to explain, keeps shape | Z-score, ranking, percentiles | Yes |
| Aggregation | Simple average | Matches equal weights | Weighted average | Yes |
| Missing data | 8-of-11 rule | Balance of coverage and trust | Complete-case, imputation | Yes |
| Grouping | K-Means | Simple and clear | Hierarchical, DBSCAN | Yes |
| Number of groups | 3 | Clear, useful middle type | 2, 4, 5 | Yes |
| Policy layer | Priority areas | Data supports areas, not schemes | Policy prescriptions | Yes |
| Scenarios | Simulations | Show "what if", not "what will" | Predictive models | Yes |
| Tools | Python, Jupyter | Repeatable and readable | Excel | Yes |
| Reports | Markdown | Version control, opens on GitHub | Word | Yes |
| Structure | Version 1 and 2 split | Stable index, growing analysis | One combined project | Yes |

A reader can use this table to revise the whole project in a few minutes.

## In one line

Good research is not about choosing the most complicated method. It is about choosing methods
that fit the question, explaining them clearly, and being honest about their limits. Every
decision in this project follows that idea.
