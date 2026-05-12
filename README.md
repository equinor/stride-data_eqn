# stride-data
STRIDE datasets ready for import.

## Historical Hourly Demand (ENTSO-E)

The `global/profile_data/historical_demand_entsoe/` dataset contains hourly total
electricity demand for European countries sourced from the ENTSO-E Transparency Platform.

### Running the download

```bash
# Prerequisites (script-level only — not needed by downstream consumers)
pip install entsoe-py pyyaml pyarrow pandas

# Set your API key (free registration at https://transparency.entsoe.eu/)
export ENTSOE_API_KEY="your-token-here"

# Download all countries and years
python scripts/download_entsoe.py

# Download specific countries/years
python scripts/download_entsoe.py --countries Germany France --years 2023 2024
```

### Data Attribution

Source: ENTSO-E Transparency Platform (https://transparency.entsoe.eu/).
Free for commercial and research use; attribution required.
Terms: https://transparency.entsoe.eu/content/static_content/Static%20content/terms%20and%20conditions/terms%20and%20conditions.html

### Ireland / UK Note

`IE_SEM` covers the Single Electricity Market (Republic of Ireland + Northern Ireland).
`GB` excludes Northern Ireland. UK national statistics typically include NI, so annual
totals for GB from ENTSO-E will be lower than UK-wide national statistics.
