# India State Competitiveness Index (ISCI)
## Final Report — Version 2.0

## Project background

Every year the government publishes a lot of data about Indian states. But the data sits in
different tables, in PDF files, in different units and different years. There is no simple,
open way to compare states on how good they are for business, using only official data.

Researchers often study single indicators, but the overall picture is hard to see. A single,
transparent and reproducible index makes comparison easier while keeping the original data
available.

This project builds one. It is called the India State Competitiveness Index, or ISCI. It
turns official data into a single score for each state, ranks the states, and then studies
what the ranking means.

## Research objective

The project has one aim: measure and explain the competitiveness of Indian states using only
official data and a well-known idea called Michael Porter's Diamond.

Version 1.0 built the index. Version 2.0 explains it: what the data looks like, how each
state performs, why states differ, and where each state could improve.

## Methodology overview

The data comes from two official sources: the RBI Handbook of Statistics on Indian States
2024-25 and the MSME Annual Report.

From these, the project uses 11 indicators. They cover two parts of Porter's Diamond: Factor
Conditions (the basic inputs, like schooling, health, jobs, power and roads) and Related &
Supporting Industries (factories, small businesses, manufacturing and investment).

Each indicator is put on the same 0 to 1 scale. Every indicator counts the same. A state's
score is the average of its indicators. A state is scored only if it has at least 8 of the 11
indicators. This gives a score for 33 states and union territories.

The ranking was tested. Changing the unemployment measure, the coverage rule, or the scaling
method makes very little difference to the order. So the ranking is stable.

The project was built with Python, Pandas and Jupyter Notebook. Python was used to automate
the data cleaning, validation, normalization and report building. This kept the work
reproducible and reduced manual mistakes.

## Project workflow

The project has two stages:

| Stage | Steps |
|-------|-------|
| Version 1.0 — Build the index | data collection, cleaning, validation, normalization, index creation |
| Version 2.0 — Understand the index | analysis, interpretation, reporting |

Version 2.0 has ten notebooks, each with one job:

| Notebook | Purpose |
|----------|---------|
| 06 | Exploratory data analysis |
| 07 | State profiles |
| 08 | Porter's Diamond interpretation |
| 09 | Comparative analysis |
| 10 | State clustering |
| 11 | Gap analysis |
| 12 | Development priorities |
| 13 | Scenario analysis |
| 14 | Research findings |
| 15 | Final report |

## Main findings

All findings come from Notebooks 06 to 14. Nothing new is added here.

1. States differ in overall competitiveness. Scores run from about 0.20 to 0.61. Goa is the
   highest and Arunachal Pradesh the lowest. The scores are close together, so the order
   matters more than the gaps.

2. States fall into three groups: strong on both parts (12 states), strong basic conditions
   but weaker industry (6 states), and weak on both parts (15 states).

3. Against the national average, most states' biggest weakness is a basic-conditions number.
   This is true for 23 of the 33 states. So a state's position today is shaped mostly by
   basic conditions.

4. Against the top group, the biggest gap is industry for 26 of the 33 states. Industry is
   also the main priority area for 26 of the 33 states. So the distance to the strongest
   states is mostly about industry.

5. Closing a state's single biggest gap raises its score by a small amount and moves its rank
   by 0 to 6 places. Weak states improve but stay near the bottom, because they still have
   other gaps.

## Overall conclusions

Two simple ideas hold the findings together:

- Basic conditions explain where a state stands against the average today.
- Industry explains the remaining distance to the strongest states.

The three groups differ mostly on industry, not on basic conditions. And improving one area
helps a little, but most states would need gains in more than one area to move much further
up.

The index should be used as a starting point for understanding state competitiveness, not
as a complete measure of development.

None of this is a new claim. Each point is a summary of what the earlier notebooks measured.

## Limitations

- The index measures two of Porter's four parts. Demand is only described with income
  figures, and firm competition is not measured.
- It uses only official data from the RBI Handbook and the MSME report. It does not include
  every factor that affects development.
- Some indicators are missing for smaller states, and small groups can move up or down more
  easily.
- The scenarios are simple simulations, not forecasts.
- The findings show links in the data. They do not prove cause.
- Equal weights assume every indicator is equally important. A different weighting method
  could give slightly different scores.

## Future work

- Add measures for Demand Conditions and Firm Strategy when reliable state-level data is
  available, for example DPIIT startup counts.
- Add more indicators to widen the picture beyond the current eleven.
- Revisit the unemployment measure if a combined state figure is published.
- Automate future data updates as new official reports are published.
- Add interactive dashboards to make the results easier to explore.
- Compare several years to study how states change over time.

## Sources

- RBI, Handbook of Statistics on Indian States 2024-25.
- Ministry of MSME, Annual Report (Udyam registrations).

All the data used in this project comes from official Government of India publications.
