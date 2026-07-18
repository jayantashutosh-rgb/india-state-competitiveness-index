"""
Canonical list of Indian states and union territories for the project, and a small
helper that maps the varied names in the source tables onto this list.

Merged administrative entities use one canonical name (Dadra & Nagar Haveli and
Daman & Diu). Canonical names carry no footnote markers. Rows that are not
geographic entities (footnotes, region rows, telecom circles) do not map here and
are dropped or flagged by the caller.
"""

CANONICAL_ENTITIES = [
    "Andaman & Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam",
    "Bihar", "Chandigarh", "Chhattisgarh", "Dadra & Nagar Haveli and Daman & Diu",
    "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir",
    "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh",
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
    "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
]

_ALIASES = {
    "Jammu And Kashmir": "Jammu & Kashmir",
    "Dadra & Nagar Haveli": "Dadra & Nagar Haveli and Daman & Diu",
    "Daman & Diu": "Dadra & Nagar Haveli and Daman & Diu",
}

_CANON = set(CANONICAL_ENTITIES)


def clean_entity(name):
    """Strip footnote markers and map known spellings to the canonical name.
    Returns None if the cleaned name is not one of the canonical entities."""
    name = str(name).strip().rstrip("*@# ").strip()
    name = _ALIASES.get(name, name)
    return name if name in _CANON else None
