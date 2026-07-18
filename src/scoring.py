"""Normalization and scoring for the competitiveness index.
Shared by Notebook 04 (build) and Notebook 05 (sensitivity), so the two stay in sync.
"""

import pandas as pd

FACTOR_CONDITIONS = ["ger", "life_expectancy", "unemployment_rate", "cd_ratio",
                     "per_capita_power", "td_losses", "road_density"]
RELATED_SUPPORTING = ["factory_density", "msme_density", "manufacturing_share",
                      "investment_rate"]
INDICATORS = FACTOR_CONDITIONS + RELATED_SUPPORTING
NEGATIVE = {"unemployment_rate", "td_losses"}


def normalize(col, negative=False):
    """Min-Max scale a column to 0-1. Negative indicators are inverted so a higher
    score always means a stronger position. Missing values stay missing."""
    lo, hi = col.min(), col.max()
    if hi == lo:
        return col.where(col.isna(), 0.5)
    scaled = (col - lo) / (hi - lo)
    return 1 - scaled if negative else scaled


def indicator_scores(df):
    """Return the 11 indicators scaled to 0-1. df must hold the INDICATORS columns."""
    return pd.DataFrame({c: normalize(df[c], c in NEGATIVE) for c in INDICATORS})


def build_index(scores, min_indicators=8):
    """Final score, rank and coverage. A state is scored only if it has at least
    min_indicators of the 11; others get no score and no rank."""
    available = scores.notna().sum(axis=1)
    overall = scores.mean(axis=1)
    overall[available < min_indicators] = float("nan")
    return pd.DataFrame({
        "competitiveness_score": overall,
        "Rank": overall.rank(ascending=False, method="min").astype("Int64"),
        "Indicators_Available": available,
        "Coverage_Percent": (available / len(INDICATORS) * 100).round().astype(int),
    })
