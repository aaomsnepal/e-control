#!/usr/bin/env python3
"""
Load historical OHLC from Nepse-All-Scraper CDN into local CSVs / future DB.
Idempotent style — safe to re-run.
"""

import csv
import requests
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).resolve().parents[2]
OHLC_DIR = BASE / "data" / "ohlc"
META_DIR = BASE / "data" / "meta"
CDN = "https://cdn.jsdelivr.net/gh/SamirWagle/Nepse-All-Scraper@main/data"

# Expand this list as needed
SYMBOLS = [
    "ADBL", "NABIL", "NICA", "SBI", "UPPER", "NHPC", "API", "NTC",
    "NMB", "EBL", "SCB", "GBIME", "PCBL", "SANIMA", "PRVU",
    "KBL", "MBL", "NICA", "SBL", "CZBIL"
]

def fetch_company_list():
    url = f"{CDN}/company_list.json"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    META_DIR.mkdir(parents=True, exist_ok=True)
    path = META_DIR / "company_list.json"
    path.write_bytes(r.content)
    print(f"Company list saved → {path}")
    return r.json()

def fetch_ohlc(symbol: str):
    url = f"{CDN}/company-wise/{symbol}/prices.csv"
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        OHLC_DIR.mkdir(parents=True, exist_ok=True)
        path = OHLC_DIR / f"{symbol}_prices.csv"
        path.write_bytes(r.content)
        lines = r.text.strip().splitlines()
        print(f"  {symbol}: {len(lines)-1} rows → {path.name}")
        return True
    except Exception as e:
        print(f"  {symbol}: FAILED ({e})")
        return False

def main():
    print(f"[{datetime.now()}] Starting historical OHLC load...")
    fetch_company_list()
    print("\nDownloading OHLC...")
    success = 0
    for sym in SYMBOLS:
        if fetch_ohlc(sym):
            success += 1
    print(f"\nDone. {success}/{len(SYMBOLS)} symbols loaded.")

if __name__ == "__main__":
    main()
