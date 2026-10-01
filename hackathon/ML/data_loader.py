import os
import requests

import numpy as np
import pandas as pd

from config import DATA_RAW

def fetch_nasa_power(region, lat, lon,
                     start_date="19910101", end_date="20251231",
                     force=False):
    """
    Fetch daily solar irradiance (ALLSKY_SFC_SW_DWN, kWh/m²/day) from NASA POWER.
    Returns a DataFrame indexed by date with column 'solar_kwh_m2'.
    """
    cache_path = os.path.join(DATA_RAW, f"nasa_daily_{region.lower()}.csv")

    if os.path.exists(cache_path) and not force:
        print(f"  [CACHE] Loading from Drive: {cache_path}")
        df = pd.read_csv(cache_path, parse_dates=["date"], index_col="date")
        return df

    print(f"  [DOWNLOAD] Fetching from NASA POWER API for {region}...")
    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "latitude":   lat,
        "longitude":  lon,
        "start":      start_date,
        "end":        end_date,
        "parameters": "ALLSKY_SFC_SW_DWN",  # Solar irradiance, kWh/m²/day
        "community":  "AG",                 # Agroclimatology
        "format":     "JSON",
    }

    try:
        response = requests.get(base_url, params=params, timeout=60)
        response.raise_for_status()
        data = response.json()

        solar_dict = data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]

        df = pd.DataFrame.from_dict(solar_dict, columns=["date", "solar_kwh_m2"])

        df.to_csv(cache_path)
        print(f"  [SAVED] {cache_path} ({len(df)} rows)")
        return df

    except Exception as e:
        print(f"  Error fetching NASA POWER for ({lat}, {lon}): {e}")
        return None

def load_hdx_rainfall(force=False):
    """
    Load HDX Syria subnational rainfall indicators.
    Saves to Drive cache after first successful load.
    """

    cache_path = os.path.join(DATA_RAW, "syr-rainfall-subnat-full.csv")

    if os.path.exists(cache_path) and not force:
        print(f"  [CACHE] Loading from Drive: {cache_path}")
        df = pd.read_csv(cache_path, parse_dates=["date"])

    else:
        print("  Download from: https://data.humdata.org/dataset/syr-rainfall-subnational")
        print("  File: syr-rainfall-subnat-full.csv (14.1 MB)")
        print(f"  Then upload to Colab or place at: {cache_path}")
        return None

    return df


def load_faostat_syria(force=False):
    cache_path = os.path.join(DATA_RAW, "faostat_syria_crops.csv")

    if not os.path.exists(cache_path):
        print(f"  [MISSING] {cache_path}")
        return None

    print(f"  [CACHE] Loading from Drive: {cache_path}")
    df = pd.read_csv(cache_path)
    return df