# Feature Engineering Spec
India State Competitiveness Index (ISCI)

Version 1.0
Date: 11 July 2026

---

This lists every variable that is computed rather than read straight from a source
table. Indicators that already arrive as a ratio or a per-capita figure (gross
enrolment ratio, life expectancy, unemployment rate, credit-deposit ratio, per
capita power availability, telephones per 100, T&D losses) are not derived and are
not listed here.

Population rule: population is derived, not taken from a table. Use it only when both
inputs are from the same year and the same price base:

Population = Total NSDP / Per Capita NSDP

The Python Function column names the function that will compute each feature during
ETL. These functions do not exist yet; they are added to src/ when the code is
written.

| Derived Feature | Formula | Purpose | Source Variables | Validation Check | Python Function |
|---|---|---|---|---|---|
| State population | Total NSDP / Per Capita NSDP | Denominator for the per-capita and density features below | Total NSDP (RBI States T23 or Economy T5), Per capita NSDP (States T19 or Economy T9) | Both inputs same year and same price base. Result positive and in a believable range. Spot-check a few states against a known total. | derive_population |
| Factory density | Factories / Population × 100000 | Compare large-industry presence across states of different size | Number of factories (T116), derived population | Population from the matching period. No divide-by-zero. Industrial states should rank high. | derive_factory_density |
| MSME density | Udyam registrations / Population × 100000 | Compare the small-enterprise base across states | MSME Udyam registrations (MSME Annual Report), derived population | Align the registration cut-off date with the population year as closely as possible. Values positive. | derive_msme_density |
| Manufacturing share of GVA | Manufacturing GVA / Total GVA × 100 | Show how large the industrial sector is within a state's economy | Manufacturing GVA (T33), Total state GVA (T25 or GSDP T21) | Both same year and price base. Result between 0 and 100. | derive_manufacturing_share |
| Investment rate | GFCF / Total GVA × 100 | Show how much new industrial investment is happening relative to size | Gross fixed capital formation (T130), Total GVA | Same year and base. GFCF is lumpy, so use a multi-year average. Values positive. | derive_investment_rate |
| Road density | Road length / Population × 100000 | Compare road provision across states | Length of roads (T146), derived population | Area-based density is not used because state area is not in the approved data. Population from the matching period. Values positive. | derive_road_density |
| Own tax revenue share | Own tax revenue / Total revenue × 100 | Government overlay: fiscal self-reliance | Own tax revenue (T168), total revenue (assembled from finance tables) | Total revenue built the same way for every state. Result 0 to 100. | derive_own_tax_share |
| Capital outlay share | Capital outlay / Total expenditure × 100 | Government overlay: development orientation of spending | Capital outlay (T174), total expenditure (assembled) | Total expenditure defined the same way for every state. Result 0 to 100. | derive_capital_outlay_share |
| Fiscal deficit share | Gross fiscal deficit / Total expenditure × 100 | Government overlay: fiscal health (lower is better) | Gross fiscal deficit (T164), total expenditure (assembled) | Include only if available on the same basis for all states, otherwise drop. | derive_fiscal_deficit_share |
