from pathlib import Path

import pandas as pd

base_dir = Path(__file__).resolve().parent.parent

COUNTRIES = {
    "country_1": "Southeastern Asia",
    "country_2": "Western Europe",
}

def main():
    df = pd.read_parquet(
        base_dir / ".." / "global" / "profile_data" / "load_shapes" / "load_data.parquet"
    )

    # filter year column to test model_years
    model_years = pd.read_csv(base_dir / "dimensions" / "model_years.csv")["id"].tolist()
    df = df[df["year"].isin(model_years)]

    # filter sectors to test sectors
    sectors = pd.read_csv(base_dir / "dimensions" / "sectors.csv")["id"].tolist()
    # map to load shape sectors
    mapping = pd.read_csv(
        base_dir / ".." / "global" / "profile_data" / "load_shapes" / "dimension_mappings" / 
        "IMAGE_load_shape_sectors_to_sectors.csv"
    )
    load_shape_sectors = mapping[mapping["to_id"].isin(sectors)]["from_id"].tolist()
    df = df[df["sector"].isin(load_shape_sectors)]

    # filter enduses
    df = df[df.enduse.isin(["cooling", "other"])]

    # filter countries and apply test country names
    regions_to_keep = list(COUNTRIES.values())
    # TEMPORARY
    # columns_to_keep = ["year", "month", "hour", "is_weekday", "sector", "enduse"] + regions_to_keep
    # df = df[columns_to_keep]
    # df = df.rename(columns={v: k for k, v in COUNTRIES.items()})
    df = df[df["geography"].isin(regions_to_keep)]
    df["geography"] = df["geography"].map({v: k for k, v in COUNTRIES.items()}) 

    # scale data
    # countries = list(COUNTRIES.keys())
    # df[countries] = df[countries] * 0.001
    df["value"] = df["value"] * 0.001

    df.to_csv(base_dir / "profile_data" / "load_shapes" / "load_data.csv", index=False)

if __name__ == "__main__":
    main()