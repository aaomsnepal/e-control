# NEPSE Data System

**Solid multi-source data platform for Nepal Stock Exchange (NEPSE)**

Designed to collect **historical (old) + live** data in a clean, scalable way.

> This is an **open architecture + working foundation**.  
> Full multi-year floorsheet + every symbol history is large — use the ingestion scripts to pull what you need.

---

## What this system gives you

- Clean folder structure
- Normalized database schema
- Multi-source configuration
- Historical download scripts
- FastAPI skeleton ready to expand
- Clear path from free/unofficial → licensed data

---

## Structure

```text
nepse-data-collection/
├── backend/               # FastAPI application
│   └── app/main.py
├── config/
│   └── sources.yaml       # All data sources in one place
├── database/
│   └── schema.sql         # Ready-to-use tables
├── data/
│   ├── ohlc/              # Historical price samples
│   ├── floorsheet/
│   ├── meta/
│   └── indices/
├── scripts/
│   ├── historical/        # Old data loaders
│   ├── live/              # Live polling (to be expanded)
│   └── utils/
├── docs/
│   ├── ARCHITECTURE.md
│   └── sources.md
└── README.md
```

---

## Quick Start

### 1. Install basics
```bash
pip install requests fastapi uvicorn pandas
```

### 2. Load more historical OHLC
```bash
python scripts/historical/load_ohlc_from_cdn.py
```

### 3. Run API skeleton
```bash
cd backend
uvicorn app.main:app --reload
```

### 4. Database
```bash
# PostgreSQL / SQLite
psql -f database/schema.sql
```

---

## Data Sources (see docs/sources.md)

**Historical**
- Aabishkar2/nepse-data
- Nepse-All-Scraper
- nepse-open-data
- ShareSansarScraper

**Live**
- nepse_data_api
- NepseUnofficialApi
- Hosted unofficial endpoints

**Production path**
- npstocks / MDP (licensed)

---

## Next Steps to make it strong

1. Load full historical base from the main GitHub repos
2. Add daily EOD cron / GitHub Action
3. Implement live polling service with caching
4. Add floorsheet ingestion + broker analytics
5. Switch critical live path to licensed feed when ready
6. Add authentication + rate limiting on your API

---

## Disclaimer

Most free sources are **unofficial**.  
They can break. For serious commercial products, use NEPSE-licensed data.

---

Built as a solid foundation. Expand it.
