# Development Priorities
India State Competitiveness Index (ISCI) — Version 2.0

**Research question:** Where should each state focus to improve?

This notebook does not recommend specific government schemes or policy mechanisms. It
identifies the areas where the data suggests that improvement would matter most. These are
evidence-based priorities from the measured gaps, not policy prescriptions.

## How the priorities are found

For each state we look at its gaps to the top group (from Notebook 11). The numbers where a
state is furthest below the top group are its priorities. Each number is then linked to a
broad area, such as industry, education or power, so the priorities are easy to read.

A note on words: we use "priority areas", not "policy". The data can show where a state is
behind. It cannot show which scheme a government should run.

## Priorities by state type

### Strong on both parts (12 states)

These states are already near the top. Their remaining gaps are small and mixed, spread
across finance, investment, manufacturing and MSMEs. For this group, the remaining gaps are
small. The focus is on improving a few specific areas rather than catching up across many
areas.

### Strong basic conditions, weaker industry (6 states)

For this group the priority is clear. Every state here has investment among its two biggest
gaps, and most also have manufacturing. Their basic conditions are already strong, so the
data points to industry and investment as the main priority.

### Weak on both parts (15 states)

Industry stands out again. Factory density is the biggest gap for most states in this
group, followed by manufacturing and investment. A few states also have education among
their gaps. So the data points to industry first, with education as a second area for some
states.

## Priorities by state

Each state's main priority (biggest gap to the top group), second priority, and smallest
gap, shown as broad areas.

Broad areas used in this table:

- Industry = factory density
- Manufacturing = manufacturing share
- Investment = investment rate
- MSMEs = MSME density
- Jobs = low unemployment
- Health = life expectancy
- Education = school enrolment
- Finance = credit-to-deposit ratio
- Power supply = per-capita power
- Power losses = transmission and distribution losses
- Roads = road density

| State | Main priority | Secondary priority | Smallest gap |
|-------|---------------|--------------------|--------------|
| Goa | Jobs | Finance | Finance |
| Tamil Nadu | Investment | Manufacturing | Power losses |
| Gujarat | Education | Health | Roads |
| Puducherry | Roads | MSMEs | Finance |
| Telangana | Manufacturing | Investment | Education |
| Andhra Pradesh | Manufacturing | Investment | Health |
| Punjab | Manufacturing | Finance | Roads |
| Maharashtra | Industry | Investment | Roads |
| Himachal Pradesh | MSMEs | Finance | Power supply |
| Haryana | Health | Power losses | Industry |
| Uttarakhand | Finance | Industry | Jobs |
| Karnataka | Investment | Industry | Power losses |
| Delhi | Investment | Manufacturing | MSMEs |
| Odisha | Industry | MSMEs | Power supply |
| Kerala | Investment | Manufacturing | Finance |
| Sikkim | Investment | Industry | Power supply |
| West Bengal | Industry | Investment | Roads |
| Rajasthan | Industry | Manufacturing | Power supply |
| Chandigarh | Investment | Manufacturing | Finance |
| Assam | Industry | Education | Jobs |
| Jharkhand | Industry | MSMEs | Manufacturing |
| Chhattisgarh | Health | Industry | Power supply |
| Mizoram | Manufacturing | Investment | Power supply |
| Madhya Pradesh | Industry | Education | Roads |
| Tripura | Investment | Manufacturing | Power supply |
| Jammu & Kashmir | Industry | Investment | Power supply |
| Uttar Pradesh | Industry | MSMEs | Power supply |
| Manipur | Manufacturing | Investment | Power supply |
| Andaman & Nicobar Islands | Industry | Manufacturing | Roads |
| Bihar | Industry | Education | Jobs |
| Meghalaya | MSMEs | Industry | Power supply |
| Nagaland | Manufacturing | Investment | Power supply |
| Arunachal Pradesh | Power losses | Manufacturing | Power supply |

The full table is saved in development_priorities.csv.

## Cross-state findings

Counting each state's main priority area:

- Industry: 11 states
- Investment: 7 states
- Manufacturing: 6 states
- MSMEs and Health: 2 states each
- Jobs, Education, Roads, Finance and Power losses: 1 state each

Putting the industry-related areas together (industry, manufacturing, investment and
MSMEs), 26 of the 33 states have an industry-related area as their main priority. This is
consistent with the gap analysis, where industry-related indicators appeared most often as
the biggest development gaps.

## Important limits

- These priorities come only from the ISCI data. They do not show which government
  programme should be used.
- They do not prove that improving one number will automatically improve another.
- A "smallest gap" area is only where a state is already close to the top group. It is not
  always the easiest thing to improve.
- The priorities point to areas, not to actions. What to actually do is a separate question,
  outside this data.
- The priorities are based only on the indicators used in this index. They do not include
  every factor that affects development.

## Questions for the next notebook

- What could happen to a state's score if it closed one of these gaps?
- Which gap would move a state up the most?

The next notebook tests these "what if" questions.
