# India State Competitiveness Index (ISCI)
## A Research Thesis on Measuring State Competitiveness Using Official Government Data

This document is the full write-up of the project. It brings together the work from all the
notebooks and the supporting documents into one place. It does not add any new analysis. Its
purpose is to bring the project's methods, findings and reflections into one complete document.
Every result comes from the notebooks, and every design choice is explained in more detail in
the supporting documents, which are named where useful.

The language is kept simple on purpose, so that a reader from any background can follow it.

---

## 1. Purpose and research question

The purpose of this project is to measure and explain the competitiveness of Indian states,
using only official government data and a well-known idea called Michael Porter's Diamond.

The project has two stages:

- Version 1.0 builds the index: it reads the data, cleans it, turns it into indicators, and
  produces a single score and ranking for each state.
- Version 2.0 explains the index: it studies what the data looks like, how each state performs,
  why states differ, and where each state could improve.

The main research question is simple:

> How competitive are Indian states, and what explains the differences between them?

A second question follows naturally: what strengths, weaknesses and patterns can be seen once
competitiveness is measured?

This large question was broken into smaller ones, and each notebook answered one of them. This
kept the work clear and stopped the notebooks from repeating each other.

## 2. Background and motivation

Every year the government publishes a large amount of data about Indian states. But the data
sits in different tables, in long PDF reports, in different units and different years. There is
no single, open and reproducible way to compare states on how good they are for business, using
only official data.

Common single numbers do not fill this gap. GDP measures the size of an economy. Per-capita
income measures average wealth. The Human Development Index measures development. None of these
is the same as competitiveness, which is about the conditions that help firms grow.

This project does not replace these existing measures. It complements them by answering a
different question.

So the motivation was to build one transparent index that:

- uses only official data, so anyone can check it,
- is based on a recognised framework, not a random mix of indicators,
- is fully reproducible, so the same data and code give the same result,
- keeps the original data available at every step, and
- documents every important decision, so readers can understand not only the result but also
  how the result was produced.

The challenge was not a lack of data. The challenge was turning many separate official reports
into one consistent picture.

## 3. Conceptual framework: Porter's Diamond

Michael Porter's Diamond is an idea about why some places are more competitive for business
than others. It looks at four parts, often called determinants:

1. Factor Conditions: the basic inputs a place gives its firms, such as skilled people, health,
   finance, power and transport.
2. Demand Conditions: the size and nature of local demand.
3. Related & Supporting Industries: the suppliers and connected industries around a firm.
4. Firm Strategy, Structure & Rivalry: how firms are organised and how strongly they compete.

Government and chance also influence these parts, but they are treated as background, not as
separate measures.

Porter was chosen because its parts can be linked to official indicators, and because it gives
a clear structure instead of a loose list. It was chosen before the data was collected, and the
data was then selected to match the framework, not the other way around.

The framework has a limit: not every part can be measured with the data available. In this
project, only two parts had reliable state-level official data, so only those two were built
into the index. Rather than estimate or guess the remaining two parts, the project measured
only what could be supported by the available evidence. This choice is explained in Section 7
and in RESEARCH_DECISIONS.md, and PROJECT_PHILOSOPHY.md explains the principles behind it.

With the framework in place, the next step is to explain the data, the indicators and the
methods used to build the index.

## 4. Data and methodology

### Data sources

The project uses two official sources: the RBI Handbook of Statistics on Indian States
2024-25, and the Ministry of MSME Annual Report. Other official documents were reviewed but
not used, because they did not cover all states or did not match the state list. Those choices
are recorded in the project's data documents.

These two sources provided the indicators used in the index. Other official reports were
reviewed mainly to check definitions, compare coverage, or explore possible future indicators.

### Indicators

From these sources, the project uses 11 indicators. They cover the two measured parts of
Porter's Diamond.

Factor Conditions (7): gross enrolment ratio, life expectancy, unemployment rate,
credit-deposit ratio, per-capita power, transmission and distribution losses, and road
density.

Related & Supporting Industries (4): factory density, MSME density, manufacturing share of
GVA, and investment rate.

The indicators were chosen before the index was built and were kept fixed throughout
Version 1.0.

### From raw data to indicators

The main source is a 472-page PDF. The numbers were pulled out with Python, using a tool
called pdfplumber. Some tables were printed sideways or across two pages, and code was written
to read even those. When a table could not be read cleanly, the code stopped instead of
guessing.

The tables were then cleaned and joined. State names were made to match one common list.
Densities and shares were worked out, for example factories per person and manufacturing as a
share of output. Where a state was missing recent figures, an earlier year was used and the
year was recorded. This handling is explained in the feature notes and in RESEARCH_DECISIONS.md.

Every important transformation was written as code rather than done by hand.

### Building the score

Every indicator was put on the same 0 to 1 scale using Min-Max scaling. Two indicators,
unemployment rate and T&D losses, are worse when higher, so they were flipped, so that a high
score always means a stronger position.

Every indicator was given equal weight, and a state's score is the average of its available
indicators. A state was scored only if it had at least 8 of the 11 indicators. This gave a
score for 33 states and union territories. Three union territories had too little data and were
left out. They were excluded only because they did not meet the project's coverage rule.

### Testing the result

The ranking was tested by changing three choices: the unemployment measure, the coverage rule,
and the scaling method. Each time, the order of the states barely changed. So the ranking is
stable and does not depend on any single choice. This does not prove the index is perfect. It
shows that the main conclusions are not driven by one technical choice.

The full build is in Notebooks 01 to 05.

With the index built and tested, the next step is to look at what it found.

## 5. Findings

All findings come from the notebooks. Nothing new is added here.

1. **States differ in overall competitiveness.** Scores run from about 0.20 to 0.61. Goa is the
   highest and Arunachal Pradesh the lowest. The scores are close together, so the order
   matters more than the gaps.

2. **States fall into three groups.** These are strong on both parts (12 states), strong on
   basic conditions but weaker on industry (6 states), and weak on both parts (15 states).

3. **Basic conditions shape a state's position today.** Against the national average, most
   states' biggest weakness is a basic-conditions number. This is true for 23 of the 33 states.

4. **Industry sets the distance to the top.** Against the top group, the biggest gap is
   industry for 26 of the 33 states. Industry is also the main priority area for 26 of the 33
   states.

5. **Closing one gap helps but does not transform a state.** Closing a state's single biggest
   gap raises its score by a small amount and moves its rank by 0 to 6 places. Weak states
   improve but stay near the bottom, because they still have other gaps.

The findings become clearer when read through Porter's framework, which is the next section.

## 6. Interpretation

This section reads the findings through Porter's Diamond. It is interpretation, so it says what
the numbers seem to show, not what they prove.

### Factor Conditions

The states strongest on basic conditions are Delhi, Tamil Nadu, Andhra Pradesh, Maharashtra and
Telangana. States with a higher Factor Conditions score also tend to have a higher overall
score, and the two move together closely (a correlation of 0.83). This is a strong
relationship, but it does not prove causation.

### Related & Supporting Industries

This part is the main driver of the ranking. It is tied to the final score more closely than
Factor Conditions (a link of 0.93), and its scores are more spread out. So a state's place in
the ranking is decided mostly by its industrial base. The leaders here are Gujarat, Goa, Tamil
Nadu, Puducherry and Haryana.

### Demand Conditions

This part is not in the index. It is described using two income figures as rough stand-ins:
total NSDP for the size of the economy, and per-capita NSDP for income per person. These are
simple proxies. Both move with the ranking, but less strongly than the two measured parts.

### Firm Strategy, Structure & Rivalry

This part could not be measured with reliable state-level official data, so no claim is made
about it. A possible future measure, such as startup counts, is noted as a limit, not filled
in.

### The overall picture

Two simple ideas hold the findings together. Basic conditions explain where a state stands
against the average today. Industry explains the remaining distance to the strongest states.
The three groups differ mostly on industry, not on basic conditions.

This interpretation follows Porter's framework and should be read alongside the measured
findings, not as separate evidence.

Interpretation is only part of the story. The next section explains the design choices behind
the project and the trade-offs they carried.

## 7. Research decisions and trade-offs

Every project could be built in many ways. A few choices shaped this one the most. Each was
made for a reason, and each carried a trade-off.

- Official data was used, so anyone can check the work. The trade-off is that official data has
  gaps and lags.
- Only two of Porter's four parts were measured, because only those had reliable state data.
  The other two were left out rather than guessed.
- Equal weights were used, because the data gives no fair basis to weight one indicator above
  another. Other methods, such as expert weights or PCA, would add assumptions.
- Min-Max scaling was chosen because it is easy to explain. Z-score was tested and gave almost
  the same ranking.
- The 8-of-11 coverage rule was used, as a middle path between dropping many states and filling
  in missing values.
- K-Means was used for grouping, because it is simple and clear, and three groups were chosen
  because they showed a useful middle type.

The common thread is to prefer the simple, honest option that a reader can check, and to be
open about its limits. These choices were made before the analysis was interpreted, so the
findings were not used to justify the methods.

Full discussion, with alternatives and a summary table, is in RESEARCH_DECISIONS.md.

## 8. Lessons learned

Building the project taught several things, each from something that actually happened. Some
lessons came from successful results. Others came from problems that had to be solved during
the project.

- About India: industry, more than basic conditions, separates the strongest states from the
  rest. A middle group is strong on basic conditions but weak on industry.
- About government data: the data is spread across reports, in different units and years. Some
  data does not match the state list, and some files could not be used because they were
  incomplete, inconsistent or did not match the project requirements.
- About research: keeping evidence and interpretation apart, and giving each notebook one
  question, kept the work clear and honest.
- About Python: automation made the work repeatable, and code that refuses to guess is safer
  than code that always produces a number.
- About documentation: writing plain notes and recording each decision made the whole project
  easy to follow and to trust.

Detailed reflections, including what surprised us and what we would do differently, are in
LESSONS_LEARNED.md.

## 9. Project philosophy

A few principles guided the work from start to finish.

- Evidence before opinion: show the numbers first, then say what they might mean.
- Never guess: leave gaps as gaps, and do not force what the data cannot support.
- Simplicity: a simple method that answers the question is better than a complex one.
- Reproducibility: the same data and code should give the same result.
- One question per notebook: this kept the work from overlapping or drifting.
- Honest limits: write down what the project cannot do, not only what it can.
- Transparency: every important decision was written down so another reader could understand
  how the project was built.

These principles are discussed fully in PROJECT_PHILOSOPHY.md.

With the methods, findings, decisions and guiding principles now explained, the final sections
discuss the limits of the project, possible future improvements, and the overall conclusion.

## 10. Limitations

Every index has limits. Stating them clearly is part of honest research.

1. Only two of Porter's four parts are measured. Demand is described with proxies, and firm
   competition is not measured.
2. The project uses only official data. It does not include every factor that affects
   development.
3. The index is a snapshot. It uses the latest available figures, which are not always from the
   same year, and it does not track change over time.
4. The findings show links in the data. They do not prove cause.
5. Equal weights are a modelling choice. A different weighting could give slightly different
   scores.
6. The scenarios are simple simulations, changing one indicator at a time. They are not
   forecasts.
7. Some indicators are missing for smaller states, and the coverage rule leaves three union
   territories unranked.

These limits do not make the project invalid. They define the questions it can answer.

## 11. Future work

The project can grow in several realistic ways:

- Add better indicators for Demand Conditions.
- Add indicators for firm rivalry, such as startup counts, when reliable state data is
  available.
- Build a multi-year panel to study how states change over time.
- Add stronger industrial indicators to widen the picture.
- Build an interactive dashboard to make the results easier to explore.
- Automate the annual update when new official reports are published.
- Bring in more official datasets to cover more of the framework.

Each improvement should keep the project's principles of transparency, reproducibility and
careful documentation.

## 12. Overall conclusion

This project does not claim to be the final measure of state competitiveness. It offers one
transparent, reproducible and evidence-based way of studying it, built from official data and a
recognised framework.

The main lesson is steady across the whole project. Basic conditions explain where a state
stands against the average today, and industry explains the distance to the strongest states.
These are patterns in the data, described carefully and openly, not proofs of cause.

Better data, better indicators and future research can improve the work. If it helps other
students, researchers or policymakers understand the data more clearly, or build something
better from it, then it has achieved its purpose.
