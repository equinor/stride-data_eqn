from pathlib import Path

import pandas as pd

base_dir = Path(__file__).resolve().parent.parent

COUNTRIES = {
    "country_1": "IR",
    "country_2": "KE",
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
    # TEMPORARY - https://github.com/dsgrid/dsgrid/issues/398
    # columns_to_keep = ["weather_year", "month", "day"] + regions_to_keep
    # df = df[columns_to_keep]
    # df = df.rename(columns={v: k for k, v in COUNTRIES.items()})
    df = df[df["geography"].isin(regions_to_keep)]
    df["geography"] = df["geography"].map({v: k for k, v in COUNTRIES.items()})

    df.to_csv(base_dir / "profile_data" / "weather_bait" / "load_data.csv", index=False)

if __name__ == "__main__":
    main()