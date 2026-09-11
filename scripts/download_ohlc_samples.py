#!/usr/bin/env python3
"""
Download sample historical OHLC data from Nepse-All-Scraper CDN.
Useful for quick backend testing.
"""

import requests
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OHLC_DIR = BASE_DIR / "data" / "ohlc"
META_DIR = BASE_DIR / "data" / "meta"

CDN = "https://cdn.jsdelivr.net/gh/SamirWagle/Nepse-All-Scraper@main/data"

# Add more symbols as needed
SYMBOLS = [
    "ADBL", "NABIL", "NICA", "SBI", "UPPER",
    "NHPC", "API", "NTC", "NMB", "EBL",
    "SCB", "GBIME", "PCBL", "SANIMA", "PRVU"
]

def download(url: str, dest: Path):
    print(f"→ {url}")
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        print(f"  Saved: {dest.name} ({len(r.content):,} bytes)")
    except Exception as e:
        print(f"  Failed: {e}")

def main():
    print("Downloading company list...")
    download(f"{CDN}/company_list.json", META_DIR / "company_list.json")

    print("\nDownloading OHLC samples...")
    for sym in SYMBOLS:
        download(
            f"{CDN}/company-wise/{sym}/prices.csv",
            OHLC_DIR / f"{sym}_prices.csv"
        )

    print("\nDone!")

if __name__ == "__main__":
    main()
