# Validation Notes — India State Competitiveness Index (Version 1.0)

## What this index measures

This index compares the competitiveness of Indian states and union territories using 11
indicators. The indicators sit under two of Porter's determinants: Factor Conditions (7)
and Related & Supporting Industries (4). In Version 1.0, 33 states and union territories
get a score after the coverage rule is applied. All the numbers come from two official
sources: the RBI Handbook of Statistics on Indian States 2024-25 and the Ministry of
MSME Annual Report.

## Indicators

Factor Conditions (7):

- gross enrolment ratio (secondary school)
- life expectancy
- unemployment rate
- credit-deposit ratio (place of use)
- per-capita power availability
- transmission and distribution losses
- road density

Related & Supporting Industries (4):

- factory density
- MSME density
- manufacturing share of GVA
- investment rate

For most indicators, a higher value is better. For two of them, unemployment rate and
T&D losses, a higher value is worse, so we flip them when scaling.

## Method

Putting all indicators on the same scale: the indicators use different units, so we
change every value to a number between 0 and 1. The smallest value becomes 0 and the
largest becomes 1. These smallest and largest values come only from the states in the
table, not from any outside target.

Calculating the final score: every indicator counts the same. We do not give extra
weight to either dimension. A state's score is the average of the indicators it has. We
also work out two dimension scores (Factor Conditions and Related & Supporting) only for
reading the results; they are not part of the final score.

Coverage rule: a state gets a score only if it has at least 8 of the 11 indicators. Each
state's `Indicators_Available` and `Coverage_Percent` are shown next to its score.

## Reference years

We used the most recent year that had data for almost all states. Different indicators
can use different years, because the official tables are updated at different times.

For the income and GVA tables (total NSDP, per-capita NSDP, total GVA, manufacturing GVA,
GFCF) we used 2022-23. The newer year 2023-24 was missing data for Gujarat, and 2024-25
was incomplete. The year used for each indicator is saved in
`data/processed/indicator_metadata.csv`.

## Unemployment

The source gives rural and urban unemployment separately, with no combined number.
Version 1.0 uses the simple average of the two. Two special cases:

- Chandigarh reports only the urban number and is treated as urban-only, since the
  territory is almost fully a city. No value is filled in.
- Andaman & Nicobar Islands has no unemployment value in the chosen series; it stays
  missing and is handled by the coverage rule.

Unit: the unemployment rate is reported per thousand people, not as a percentage. The
values are kept as they are, because putting numbers on the same scale removes the effect
of the unit anyway.

## Exclusions

Three union territories fall below the coverage rule and get no score: Dadra & Nagar
Haveli and Daman & Diu (4 of 11), Lakshadweep (5 of 11), and Ladakh (7 of 11).

Telephones per 100 is left out because it is reported by telecom circle, not by state.

Total NSDP, per-capita NSDP and GVA levels are used only to work out other features
(population, densities, shares, investment rate) and are not scored directly.

## Reading the results

The scores are close together, roughly 0.20 to 0.61. No state is best at everything, so
averaging brings the scores near the middle. The order of the states is more useful than
the difference between their scores.

Andaman & Nicobar Islands is at the coverage minimum (8 of 11), so its score is based on
fewer indicators. This shows in its Coverage_Percent.

States can do well on one dimension and less well on the other. Looking at
`dimension_scores.csv` along with the ranking helps explain where a state's score comes
from.

## Top and bottom of the ranking

The five highest-ranked states and the five lowest-ranked states can be seen directly in
`competitiveness_index.csv`.

The ranking should be read together with `dimension_scores.csv`. A high or low overall
rank does not always mean a state does the same on every indicator. Many states are
strong in some areas and weaker in others, so the dimension scores add useful context.

## Sensitivity checks

We ran three checks, and all gave the same picture.

Spearman correlation is a number that tells us how similar two rankings are. A value near
1 means the two rankings are almost the same.

Unemployment: using rural, urban or the average gave almost the same ranking. The
Spearman correlation between the three was 0.99 or higher. The top 10 states stayed the
same in all three. Only one state changed near the bottom, where Chhattisgarh and Madhya
Pradesh swapped places around rank 23.

Coverage rule: changing the rule from 8 of 11 made very little difference. At 7 of 11,
Ladakh came in. At 9 of 11, Andaman & Nicobar went out. No other state changed.

Scaling: Min-Max and Z-score gave almost the same ranking, with a Spearman correlation of
0.99. The top and bottom states stayed the same, and only a few middle states moved a
little.

These checks show that changing the unemployment measure, the coverage rule or the
scaling method makes very little difference to the final ranking.

## Limitations

Every index has some limits.

- Only two of Porter's four determinants are included in Version 1.0.
- Some official tables do not cover every state.
- Telecom data is left out because it is reported by telecom circle, not by state.
- The index uses the latest official data available, which is not always from the same
  year.
- The index is meant to compare states, not to measure a state's full economic
  performance.

## Sources

- RBI, Handbook of Statistics on Indian States 2024-25.
- Ministry of MSME, Annual Report (Udyam registrations).
