# Data Decisions
India State Competitiveness Index (ISCI)

A running log of data-level choices made during extraction, kept for
reproducibility. It records which source table or series was used where more than
one option exists, and why.

This document records implementation decisions only. It does not define the project
methodology, which is documented separately. Each decision includes the chosen
option, the alternative considered, and the reason for the choice.

---

## Credit-Deposit Ratio (place of utilisation vs place of sanction)

The Credit-Deposit Ratio based on Place of Utilisation (Table 154) is used in the
index because it reflects where credit is actually deployed in the economy.

Alternative considered:
- Table 153 (Place of Sanction)

Reason for not selecting it:
Credit may be sanctioned in one state but deployed in another, especially for large
corporate borrowers. The utilisation series better reflects where credit supports
economic activity.

The Place of Sanction series (Table 153) is retained only as a reference dataset for
reproducibility and possible sensitivity analysis.

- Index indicator: cd_ratio_utilisation.csv (Table 154)
- Reference only: cd_ratio_sanction.csv (Table 153)

## Unemployment rate (rural vs urban)

Tables 8 and 9 report the usual-status unemployment rate as separate sub-blocks:
rural (male, female, overall) in Table 8, and urban (male, female, overall) in
Table 9. No combined rural-plus-urban figure is published, and a correct
combination would need population weights that are not available here.

Both "overall" series are extracted and saved (unemployment_rural_overall.csv and
unemployment_urban_overall.csv).

Reason:
The extraction stage preserves both official series without combining them. Any
derived unemployment indicator will be documented separately during feature
engineering.

## MSME Udyam registrations (three union territories added manually)

The state-wise Udyam registration table (Micro, Small, Medium, Total) is read
directly from the MSME Annual Report. Thirty-three rows are parsed automatically,
and each is accepted only when Total equals Micro plus Small plus Medium.

Three union territories are added by hand because their names wrap across two lines
in the PDF, or have blank sub-values, which the automatic parser could not read
reliably:

- Andaman & Nicobar Islands: 21,645 / 156 / 4 / 21,805
- Dadra & Nagar Haveli and Daman & Diu: 33,931 / 916 / 135 / 34,982
- Lakshadweep: 2,431 / blank / blank / 2,431

Each value was read from the source table and checked (Total equals the sum of the
parts; Lakshadweep reports only micro units). The result is 36 states and union
territories.

## Telephones per 100 (telecom circles, not states)

Table 149 reports telephones per 100 by telecom circle, not by state. Some entries
are metro circles (Delhi, Mumbai, Kolkata, Chennai) reported separately from their
states, some combine several states (North East-I, North East-II), and some states
are grouped into one circle (for example Uttar Pradesh). Only 28 circle-level rows
are present, and they do not map cleanly to the 36 states and union territories.

The series is saved as extracted (telephones.csv). Its use as the digital
infrastructure indicator is deferred to feature engineering, where we decide either
to map circles to states with stated assumptions, or to drop it. This follows the
project's rule of not forcing a weak or mismatched measure into the index.

## Canonical entity list and name harmonization

Notebook 03 maps every source table onto one canonical list of 36 states and union
territories, defined in src/entities.py. The rules are:

- Footnote markers (*, @, #) are stripped from names.
- Spelling variants are mapped, for example "Jammu And Kashmir" becomes
  "Jammu & Kashmir".
- Merged entity: "Dadra & Nagar Haveli" and "Daman & Diu" both map to the single
  canonical name "Dadra & Nagar Haveli and Daman & Diu". Where a table still reports
  them separately (older years), the two rows are combined per indicator during
  feature engineering (sum for counts, average for rates).
- Rows that are not geographic entities are dropped or flagged, never forced into a
  state name:
  - Footnote lines such as "*: Since" and "-: Not Available ...".
  - "Jammu & Kashmir and Ladakh" in the T&D losses table (a pre-2019 combined
    series) is flagged for a later decision.
  - Telecom circles in the telephones table (Delhi, Mumbai, Kolkata, Chennai,
    North East-I, North East-II, Uttar Pradesh (E&W)) are kept out of the state
    mapping and handled separately.

This step only standardises names. Which entities finally enter the index is decided
later, and only if the methodology requires it.

## Feature selection (Notebook 03)

Reference year: most indicators use their latest official observation, chosen as the
latest year with at least 90 percent of that indicator's best state coverage. A single
common year across all indicators is not enforced because no such year exists in the
source.

The NSDP and GVA family (total NSDP, per-capita NSDP, total GVA, manufacturing GVA,
GFCF) is pinned to 2022-23, the latest year with complete state coverage. The 2023-24
series omits Gujarat and 2024-25 is provisional with substantially lower coverage.
Without this, Gujarat drops out of every income and GVA based feature.

Derived features use the same reference year for the numerator and denominator where
both come from this family: population is total NSDP (2022-23) over per-capita NSDP
(2022-23), manufacturing share is manufacturing GVA (2022-23) over total GVA (2022-23),
and investment rate is GFCF (2022-23) over total GVA (2022-23). Density features divide
a count by the 2022-23 reference population; the count itself uses its own latest year
(factories 2023-24, roads 2020, MSME 2026). The year used for each indicator is recorded
in indicator_metadata.csv.

Education (GER): the enrolment table reports the gross enrolment ratio by level
(Foundational, Preparatory, Middle, Secondary) and by sex. It does not report higher
secondary (Class XI-XII) separately; Secondary covers Class IX-XII. The index uses
Secondary Total (both sexes), the closest available measure of secondary schooling
reach.

Unemployment: no official combined rural-plus-urban series exists. Rural overall and
urban overall are both kept as separate candidate features. The final choice is
postponed to modelling and EDA, and will be recorded then.

Telephones: dropped in Version 1.0. The table is by telecom circle, not state, and
mapping circles to states would add assumptions and noise. A state-level replacement
may be added in a later version.

## Unemployment indicator (Notebook 04)

The index needs one unemployment figure per state, but the source publishes separate
rural and urban series with no combined value. Version 1.0 uses the simple average of
the rural overall and urban overall rates, named unemployment_rate. This will be
revisited if a population-weighted state figure becomes available.

Two states need special handling:

- Chandigarh reports only the urban unemployment series. Since the territory is almost
  entirely urban, the urban overall unemployment value is used as the unemployment
  indicator. No imputation is performed.
- No unemployment value is reported for Andaman & Nicobar Islands in the selected
  series. The value remains missing and is handled by the coverage rule.

Unit: the usual-status unemployment rate is reported by the RBI source in per thousand
persons, not percentage. Values are kept in the original unit because Min-Max
normalization is scale-invariant.

---

## Decision Template

Future data decisions should follow the same format:

- Decision
- Options considered
- Selected option
- Reason
- Impact on the project
