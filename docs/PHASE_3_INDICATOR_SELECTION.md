# Phase 3: Indicator Selection
India State Competitiveness Index (ISCI)

Version 1.0
Date: 11 July 2026

---

## Purpose

This document sets the rules for choosing indicators, and it will hold the
selected indicators for each determinant as we work through them. Method first,
then the choices. There is no code here; selection is a design decision recorded
for the project.

## Objective

Select the smallest set of high-quality indicators that best represents Porter's
framework using the official data cleared in Phase 0. The aim is not to include
every available variable. A tight, well-justified set is better than a long one.

## Selection principles

1. Each indicator maps to exactly one determinant, so the structure stays clean
   and nothing is placed twice.
2. Only sources cleared in Phase 0 are used (RBI States Handbook, RBI Economy
   Handbook, MSME Udyam table). Broken or reference-only files are not used.
3. Every indicator records its source, table, and year, so any number can be
   traced back.
4. Verified data comes first. Data that is Not Yet Verified is included only after
   it has been extracted and checked.
5. Each indicator has a stated direction: higher is better, or lower is better.
   This is fixed now so normalisation later does not go wrong.
6. State and year coverage is checked so that states can be compared fairly.
7. The two open Phase 0 decisions (the output measure or GSDP, and startup counts)
   are raised when the related determinant comes up, not before.
8. Every indicator carries a clear justification. For each one we state why this
   indicator, which Porter determinant it represents, and why it is a better
   choice than other available options.
9. Duplicate information is avoided. If two indicators measure almost the same
   thing, only one is kept, unless there is a strong analytical reason for both.
   This keeps out unnecessary multicollinearity and double counting.
10. Every indicator is classified before it is selected (see the fields below).

## Classification recorded for every indicator

Before an indicator is accepted, we record:

- Determinant
- Variable type (economic, infrastructure, labour, finance, industry, and so on)
- Unit
- Year
- Geographic level
- Direction (positive or negative)
- Data source
- Table number
- Verification status

## Framework decisions

These are permanent decisions that govern how income and the determinants are
treated.

Income measure, resolved. Per capita NSDP or GSDP is not part of the
competitiveness index. It is used only for external validation and interpretation
after the index is built, so it never appears inside any determinant. This removes
double counting at the source: a variable used for validation cannot also be an
index indicator. The only sub-question left is which series fills the validation
role, the correct GSDP file or RBI NSDP. That choice is still open and does not
affect how the index is built.

Demand Conditions scope. Demand conditions here represent the characteristics of
the home market that influence firms, not the economic outcomes those firms
generate. Direct state-level measures of demand sophistication are not available in
the approved datasets, so this determinant is represented only by indicators that
can be theoretically justified. Weak or artificial proxies will not be added just
to raise the count.

Unequal indicator counts are allowed. The four determinants need not carry the same
number of indicators. If factor conditions has eight strong indicators and demand
conditions has two or three defensible ones, that is acceptable. The quality of
representation matters more than symmetry across determinants.

Still open from Phase 0: whether a working state-wise startup file will be
provided. This is raised at the determinant where it matters (firm strategy and
rivalry).

## What comes next

Indicators are chosen determinant by determinant, starting with factor conditions.
Each choice carries the justification required by principle 8 and the full
classification required by principle 10.

---

## Determinant 1: Factor Conditions

### Concept

Factor conditions are the inputs a state has for production. Porter groups them
into human resources, physical resources, knowledge resources, capital resources,
and infrastructure, and argues that advanced, created factors matter more for
lasting competitiveness than basic, inherited ones. The purpose of indicator
selection is to represent these dimensions using measurable and verifiable
state-level variables from the approved data sources. This determinant measures
the quality of productive capacity available within a state, not the economic
outcomes produced by it.

### Screening

All candidates were drawn from the RBI States Handbook, then scored on eight
criteria as a decision-support step: relevance, data quality, comparability,
redundancy, interpretability, time consistency, actionability, and independence.
These scores are decision-support only. They are not weights and do not affect the
index calculation; they exist to make selection transparent and reproducible.
Scores for data quality, comparability, and time consistency are provisional until
the tables are extracted and verified.

Legend: S = Strong, M = Moderate, W = Weak. For redundancy, W is the good case
(little overlap with other indicators).

| Indicator | Group | Table | Rel | Qual | Comp | Redun | Interp | Time | Act | Indep |
|---|---|---|---|---|---|---|---|---|---|---|
| Gross Enrolment Ratio | Education | T1 | S | M | S | M | S | M | S | M |
| Gender Parity Index of GER | Education | T12 | M | M | S | S | M | M | S | W |
| Life expectancy | Health | T7 | M | M | S | M | S | S | M | M |
| Infant mortality rate | Health | T4 | M | M | S | M | S | S | S | M |
| Unemployment rate | Labour | T8/T9 | M | M | S | W | S | S | M | M |
| Rural wage rate | Labour | T112-115 | M | W | M | W | M | M | M | M |
| Doctors and specialists | Health | T16 | M | M | M | M | S | W | S | M |
| Govt hospitals and beds | Health | T17 | M | M | W | S | S | W | S | W |
| Public expenditure on health | Health | T18 | W | M | W | M | M | M | S | W |
| Forest and tree cover | Natural | T100/101 | W | M | M | W | M | W | W | M |
| Groundwater extraction | Natural | T107 | W | M | M | W | W | W | M | M |
| Annual rainfall | Natural | T102 | W | M | M | W | M | M | W | S |
| Schools and facilities | Knowledge | T151 | M | M | M | M | M | W | S | M |
| Bank offices | Finance | T152 | M | M | W | S | S | S | M | W |
| Deposits (SCBs) | Finance | T155 | M | M | W | S | S | S | M | W |
| Credit (SCBs) | Finance | T156 | S | M | W | M | S | S | M | M |
| Credit-Deposit ratio | Finance | T153/154 | S | M | S | M | M | S | M | S |
| Credit to industry | Finance | T158 | S | M | W | M | S | M | M | M |
| Personal loans | Finance | T159 | W | M | W | M | M | M | W | W |
| Regional rural banks | Finance | T160-163 | W | M | W | S | M | M | M | W |
| Per capita power availability | Energy | T138 | S | M | S | M | S | M | S | S |
| Power installed capacity | Energy | T140 | S | M | W | S | S | M | S | W |
| Power requirement/supply | Energy | T141/142 | M | M | M | S | M | M | M | W |
| Renewable capacity | Energy | T143 | M | M | W | M | M | W | S | M |
| T&D losses | Energy | T148 | M | M | S | W | M | M | S | S |
| National highways length | Transport | T144 | M | M | W | S | S | M | M | W |
| Railway route | Transport | T145 | M | M | W | M | S | M | W | M |
| Length of roads | Transport | T146 | S | M | W | S | S | M | S | M |
| State highways | Transport | T147 | M | M | W | S | S | M | S | W |
| PMGSY roads | Transport | T150 | M | M | W | S | M | M | S | W |
| Telephones per 100 | Digital | T149 | S | M | S | W | S | M | M | S |

### Table A: Final selected indicators

| Indicator | Group | Measures | Why factor conditions | Table | Dir | Status | Feature Engineering Required? |
|---|---|---|---|---|---|---|---|
| Gross Enrolment Ratio | Education | Share of eligible children enrolled | Education base of the workforce | T1 | + | Not Yet Verified | No |
| Life expectancy | Health | Average years of life at birth | Health of the productive population | T7 | + | Not Yet Verified | No |
| Unemployment rate | Labour | Share of labour force unemployed | Availability and use of labour | T8/T9 | - | Partly (T8 rural-male) | No |
| Credit-Deposit ratio | Banking and Finance | Credit as a share of deposits | Access to and deployment of capital | T153/154 | + | Not Yet Verified | No |
| Per capita power availability | Energy | Power available per person | Energy availability | T138 | + | Not Yet Verified | No |
| T&D losses | Energy | Transmission and distribution losses | Energy system efficiency | T148 | - | Not Yet Verified | No |
| Road length | Transport | Total road length (to be converted to road density during feature engineering) | Transport connectivity | T146 | + | Not Yet Verified | Yes |
| Telephones per 100 | Digital | Phones per 100 people | Communication infrastructure | T149 | + | Not Yet Verified | No |

Note on unemployment rate: Although unemployment is commonly treated as an economic
outcome, this project uses it as a labour market indicator representing the
effective utilisation of available human resources within Porter's Factor
Conditions.

Fallback: Infant mortality rate (T4, direction negative) is held as the documented
fallback health indicator. If life expectancy cannot be verified, or lacks
sufficient state coverage during extraction, IMR replaces it.

### Table B: Rejected indicators

| Indicator | Reason |
|---|---|
| Gender Parity Index of GER | Duplicates GER; measures equity, a facet of enrolment |
| Schools and facilities | Weak, absolute proxy; better represented by GER |
| Doctors and specialists | Health-service infrastructure; health represented by life expectancy |
| Govt hospitals and beds | Duplicates doctors; single-date, poor comparability |
| Public expenditure on health | Mostly government spending; fits the Government factor |
| Rural wage rate | Ambiguous direction, rural-only; poor comparability |
| Forest and tree cover | Weak theoretical link; inherited natural factor |
| Groundwater extraction | Weak link to productive capacity |
| Annual rainfall | Exogenous, not actionable; weak link |
| Bank offices | Absolute count; duplicates the finance dimension |
| Deposits (SCBs) | Absolute; largely a consequence of income |
| Credit (SCBs) | Absolute; overlaps Credit-Deposit ratio |
| Credit to industry | Overlaps finance dimension; absolute, weaker comparability |
| Personal loans | Consumer credit; weak link to productive capacity |
| Regional rural banks | Duplicates SCB banking already covered |
| Power installed capacity | Absolute; duplicates per-capita power availability |
| Power requirement/supply | Duplicates the energy dimension |
| Renewable capacity | Narrow, specialised; duplicates energy availability |
| National highways length | Central subject; subset of the road network |
| Railway route | Central subject; low state actionability |
| State highways | Subset of total roads |
| PMGSY roads | Rural subset of roads |

### Why this set

The full list held heavy redundancy and many absolute totals that do not compare
fairly across large and small states. The eight selected indicators cover the
distinct parts of factor conditions: education, health, labour, access to capital,
energy, transport, and digital infrastructure. Energy carries two complementary
measures, availability (per capita power) and efficiency (T&D losses), because they
capture different things. Most indicators are ratios or per-capita measures, so
states compare fairly and multicollinearity stays low. The set also works from
three angles: clean, low-overlap variables for the data-science work; recognised
productivity inputs for the economics; and levers that policy can actually move.

Two limitations are recorded. Knowledge resources (research, higher education,
innovation) are weakly represented, because the approved sources hold no direct
state-level data for them. All eight indicators are still Not Yet Verified or only
partly verified, so each must be extracted and checked before use, and the road
length indicator must be converted to road density during feature engineering.
Infant mortality rate is kept as a documented fallback for the health indicator.

---

## Determinant 2: Demand Conditions

Status: Not operationalised in Version 1.0.

### Concept

Demand conditions concern the characteristics of the home market that influence
firms: the size of home demand, and its sophistication, meaning how demanding and
discerning local buyers are. In Porter's argument, demanding home customers push
firms to improve quality, innovate, and raise productivity.

### Why Demand Conditions Was Not Operationalised

We evaluated every candidate the approved sources offer and found none that gives a
theoretically sound and comparable state-level measure of home demand.

- Domestic tourist visits (T13) measures tourism activity, not home-market demand.
  It is narrow, and as an absolute count with no state population available, it is
  not comparable across states.
- Exports (T181) and foreign tourist visits (T182) are external demand, not home
  demand.
- CPI inflation (T108) measures price movement, not the size or sophistication of
  demand.
- MPI poverty (T10) is an outcome and an indirect, inverse purchasing-power signal,
  not a demand measure.

No suitable, verified state-level population dataset was identified within the
approved data sources for Version 1.0. The approved sources also hold no household
consumption data and no measure of demand sophistication. Home market size can
therefore only be proxied weakly, and home market sophistication cannot be measured
at all.

Rather than fill the determinant with a weak proxy, we leave it unmeasured in this
version. Choosing "no valid measure available" over a weak measure keeps the index
honest and defensible.

This is a methodological decision, not a limitation of Porter's theory. Demand
conditions remains part of the conceptual framework. It is intentionally excluded
from the numerical index in Version 1.0 because suitable official indicators are not
available in the approved data sources.

### Version 1.0 design decision

Demand conditions is recorded as not operationalised in Version 1.0. A future
version may operationalise it if suitable official state-level data becomes
available, for example NSS or HCES consumption surveys or Census urbanisation data,
subject to approval.

---

## Determinant 3: Related and Supporting Industries

### Concept

This determinant asks whether a state has a web of industries and suppliers that
support one another. Where connected industries and supply chains are present and
strong, often clustered together, firms gain support, faster information, and shared
capabilities they could not build alone. In short, it measures the presence and
strength of a state's industrial ecosystem, not the money that ecosystem earns.

### Candidates and screening

Candidates were drawn from the ASI tables (T116 to T137), the sectoral state value
added tables (T25 to T52), the MSME Annual Report, and the supporting-infrastructure
tables (T95 to T98). They were placed in six conceptual groups and scored on nine
criteria: the eight used for factor conditions plus structural redundancy, which
asks whether a variable mainly repeats an industrial concept (scale, capacity,
investment, activity, or output) already captured by another. The groups were
industrial presence, industrial employment, industrial capital, industrial
performance, industrial ecosystem (MSME and MSSI), and supporting industrial
infrastructure. The aim was one representative per distinct concept, not every
industrial statistic.

### Table A: Final selected indicators

| Indicator | Conceptual group | Represents | Source and table | Dir | Feature Engineering | Status |
|---|---|---|---|---|---|---|
| Number of factories | Industrial presence | Large-industry presence | RBI States, T116 | + | Yes, factory density (per lakh population or per area) | Not Yet Verified |
| MSME Udyam registrations | Industrial ecosystem | Small-enterprise presence | MSME Annual Report | + | Yes, per capita | Partly Verified |
| Manufacturing share of GVA | Industrial structure | Industrial weight in the economy | Derived from GVA (T33 and total state GVA) | + | Yes, derived feature | Not Yet Verified |
| Gross fixed capital formation | Industrial capital (flow) | Investment dynamism | RBI States, T130 | + | Yes, per capita or share of GVA | Not Yet Verified |

### Manufacturing share of GVA is a derived feature

This indicator is computed, not read from a table:

Manufacturing Share (%) = Manufacturing GVA / Total GVA × 100

A structural share is conceptually different from absolute output. Absolute
manufacturing GVA records how much a state produces, which is an outcome and scales
with the size of the state. The share records how large the industrial sector is
relative to the state's whole economy, that is, how industrialised the economy is.
Two states with very different output levels can share the same industrial
structure, and a small state can be more industrialised than a large one. Using the
share keeps the indicator comparable across states and consistent with the decision
to exclude absolute output levels from the index.

### Gross fixed capital formation: justification against alternatives

GFCF is kept to represent investment dynamism, the rate at which industry adds new
productive assets. It was compared with the strongest alternatives.

- Invested capital and fixed capital are stock measures. They record accumulated
  capital, which is a measure of industrial size and moves closely with the number
  of factories already in the set. They describe how big the base is, not how
  actively it is growing.
- Industrial employment measures labour absorption, not investment, and also tracks
  industrial scale.

Only capital formation is a flow: it captures new investment made during the year,
which is what dynamism means. Gross fixed capital formation is preferred over its net
and gross-capital-formation variants because it is the standard, more stable
investment-flow measure and does not depend on depreciation estimates or inventory
swings. The stock and employment alternatives were therefore rejected for this slot;
they would duplicate the scale already captured by number of factories. One caveat:
capital formation can be lumpy from year to year, so it should be read as a
multi-year average or as a share of GVA during feature engineering.

### Table B: Rejected indicators

| Indicator | Reason |
|---|---|
| Number of workers (T122) | Duplicates industrial scale; correlated with presence |
| Total persons engaged (T123) | Industrial employment overlaps presence and structure |
| Number of employees (T132) | Duplicates persons engaged |
| Number of mandays (T133) | Labour input; duplicates employment; low actionability |
| Fixed capital (T117) | Capital stock; measures size, not dynamism |
| Working capital (T118) | Duplicates capital stock |
| Physical working capital (T119) | Duplicates capital stock |
| Productive capital (T120) | Duplicates capital stock |
| Invested capital (T121) | Capital stock; measures size, not dynamism |
| Net fixed capital formation (T129) | Duplicates gross fixed capital formation |
| Gross capital formation (T131) | Duplicates gross fixed capital formation |
| Total input (T125) | Input cost; duplicates output scale |
| Value of gross output (T126) | Absolute output; manufacturing share preferred |
| Net value added, ASI (T127) | Duplicates value added |
| Gross value added, ASI (T128) | Absolute output level; represented by manufacturing share |
| Total emoluments (T124) | Wages; duplicates employment and output |
| Industry GVA (T41/43) | Overlaps manufacturing share |
| Construction GVA (T37/39) | Sector-specific; not core industrial ecosystem |
| Services GVA (T49/51) | Services, not industrial ecosystem |
| Financial services GVA (T45/47) | Overlaps finance in factor conditions |
| Agriculture GVA (T29/31) | Agriculture, not industrial ecosystem |
| MSSI number of units (T134) | Duplicates MSME Udyam registrations |
| MSSI total investments (T135) | Older series; duplicates industrial capital |
| MSSI total production (T136) | Older series; duplicates output |
| MSSI total employment (T137) | Older series; duplicates employment |
| Cold storage capacity (T98) | Narrow, agri-specific supporting infrastructure |
| Storage capacity of foodgrains (T96) | Agri storage; weak relevance |
| RIDF sanctions (T95) | Rural infra finance; weak relevance to industrial ecosystem |

### Why this set

The four selected indicators cover complementary facets of the industrial ecosystem
with minimal overlap: large-industry presence (number of factories), the
small-enterprise base (MSME registrations), the industrial weight of the economy
(manufacturing share of GVA), and investment dynamism (gross fixed capital
formation). The large ASI families, employment, capital stock, and output levels,
were set aside because within each family the variables are near-identical and highly
correlated; keeping one representative concept per idea avoids multicollinearity. The
derived manufacturing share was preferred over raw GVA because a share compares
fairly across states and captures structure rather than output level.

### Representation limitations

- The determinant rests on formal, registered industry (ASI, MSME). Informal and
  unregistered supplier networks and clusters are not captured.
- "Related and supporting industries" ideally means supplier linkages and
  clustering. Official data does not measure inter-industry linkages or agglomeration
  directly, so this is proxied by presence, structure, and investment.
- The MSSI series overlaps MSME Udyam registrations. The current Udyam registrations
  were chosen; the older MSSI series is noted as an alternative.
- Three of the four indicators are Not Yet Verified. Each must be extracted and
  checked, and all four need feature engineering before use.

### Summary box

- Candidates evaluated: 32
- Selected: 4
- Rejected: 28
- Feature engineering required: all 4 (density, per capita, share, investment rate)
- Verification status: 3 Not Yet Verified, 1 Partly Verified (MSME Udyam)

---

## Determinant 4: Firm Strategy, Structure and Rivalry

Status: Not operationalised in Version 1.0.

This determinant is about how firms in a state are built and run, and how hard they
compete with each other. Tough local competition pushes firms to get better.

We could not measure it from the approved data. What we looked at, and why each was
dropped:

- Exports (T181) are a result of firms already being competitive, not a cause of it.
  They also say nothing about competition inside a state, and using an export figure
  would pull an output measure back into the index.
- IEM proposed investment shows intent to start new industrial projects. That is a
  partial entrepreneurship signal at best, and it does not measure rivalry, so we do
  not use it just to avoid an empty slot.
- There is no direct measure of competition or rivalry in the approved data.
- State-wise startup counts would be the right measure of firm formation, but the
  source CSV is broken and the DPIIT report gives only national totals.

So the determinant stays in the framework but is left out of the numerical index
for now. Startup density is planned for Version 1.1, once a working state-wise
startup dataset is available.

## Government (influencing factor overlay)

Government is not one of the four determinants. It affects all of them, so it does
not get its own score inside the index. We keep it beside the index as an overlay:
reported on its own and used to help read the results.

The overlay is three budget ratios. Each is built from figures inside the state
budget, so states compare directly without needing population or GSDP.

- Own tax revenue divided by total revenue. How much of its money a state raises
  itself.
- Capital outlay divided by total expenditure. How much spending goes into building
  assets rather than day-to-day running costs.
- Fiscal deficit divided by total expenditure. A rough read on fiscal health, where
  lower is better. If this one cannot be built on the same basis for every state, we
  drop it and keep the first two.

Numerator tables: own tax revenue (T168), capital outlay (T174), gross fiscal
deficit (T164). The totals (total revenue, total expenditure) are assembled from the
state finance tables during extraction. All Not Yet Verified until pulled and
checked.

## Phase 3 status

Indicator selection is complete for Version 1.0.

- Operationalised: Factor Conditions (8 indicators), Related and Supporting
  Industries (4 indicators).
- Not operationalised in Version 1.0: Demand Conditions; Firm Strategy, Structure
  and Rivalry.
- Government: overlay only, not scored.

Phase 3 is frozen.
