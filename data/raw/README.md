# data/raw

Place the approved source files here by hand. The project must run from these local
files, so nothing is downloaded or copied automatically.

Raw source files are never modified. All cleaning happens inside the ETL pipeline.
The original files remain unchanged throughout the project.

For Version 1.0 the code needs two files. Save them with these exact names so the
notebooks can find them:

- rbi_states_handbook_2024_25.md  (RBI Handbook of Statistics on Indian States 2024-25)
- msme_annual_report_2025_26.md   (Ministry of MSME Annual Report 2025-26)

Optional, kept only as a cross-check for the NSDP figures:

- rbi_economy_handbook_2023_24.md  (RBI Handbook of Statistics on the Indian Economy 2023-24)

The RBI States Handbook carries most of what Version 1.0 needs: the factor-condition
indicators, factories, roads, power, banking, state finances, the NSDP and GSDP
tables used to derive population, and the sectoral GVA tables. The MSME report
supplies the state-wise Udyam registration counts.

Do not commit large binary source files if the repository is shared publicly; keep
them local and note their official source instead.
