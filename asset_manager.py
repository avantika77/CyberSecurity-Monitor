import pandas as pd


def load_assets():
    """Load the asset inventory."""

    file_path = "data/assets.csv"

    assets = pd.read_csv(file_path)

    return assets


def get_asset_summary(assets):
    """Return basic asset statistics."""

    summary = {
        "total_assets": len(assets),
        "critical_assets": len(
            assets[assets["criticality"] == "Critical"]
        ),
        "high_assets": len(
            assets[assets["criticality"] == "High"]
        ),
        "medium_assets": len(
            assets[assets["criticality"] == "Medium"]
        ),
    }

    return summary