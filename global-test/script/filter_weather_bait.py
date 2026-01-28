from pathlib import Path

import pandas as pd

base_dir = Path(__file__).resolve().parent.parent

COUNTRIES = {
    "country_1": "Ireland",
    "country_2": "Kenya",
}

def main():
    df = pd.read_parquet(
        base_dir / ".." / "global" / "profile_data" / "weather_bait" / "load_data.parquet"
    )

    # filter weather_year column to test weather_years
    weather_years = sorted(pd.read_csv(base_dir / "dimensions" / "weather_years.csv")["id"].tolist())
    df = df[(df["weather_year"] >= weather_years[0]) & (df["weather_year"] <= weather_years[-1])]

    # filter countries and apply test country names
    regions_to_keep = list(COUNTRIES.values())
    df = df[df["country"].isin(regions_to_keep)]
    df["country"] = df["country"].map({v: k for k, v in COUNTRIES.items()})

    df.to_csv(base_dir / "profile_data" / "weather_bait" / "load_data.csv", index=False)

if __name__ == "__main__":
    main()