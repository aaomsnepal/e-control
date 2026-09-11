# NEPSE Data System — Architecture

## Goal
Build the most complete, reliable, and maintainable open NEPSE data platform possible using publicly available sources + clear path to licensed feeds.

## Core Principles
1. **Multi-source** — Never depend on a single source
2. **Historical + Live** separation
3. **Idempotent ingestion** — Safe to re-run
4. **Normalized schema** — Easy for any backend/frontend
5. **Observable** — Logging + status tracking
6. **Legal awareness** — Clear distinction between unofficial and licensed data

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Data Sources                           │
│  Historical Repos  │  Unofficial APIs  │  Licensed Feeds    │
└──────────────┬──────────────────┬───────────────┬───────────┘
               │                  │               │
               ▼                  ▼               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Ingestion Layer                           │
│  scripts/historical/   scripts/live/   adapters/            │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   Storage Layer                             │
│  PostgreSQL / TimescaleDB / ClickHouse / SQLite (dev)       │
│  - companies, daily_prices, floorsheet, indices, status     │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   API Layer (FastAPI)                       │
│  /prices  /floorsheet  /indices  /companies  /health        │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              Consumers (Dashboard / Quant / Mobile)         │
└─────────────────────────────────────────────────────────────┘
```

---

## Recommended Tech Stack

| Layer          | Choice                          | Why |
|----------------|---------------------------------|-----|
| Database       | PostgreSQL + TimescaleDB        | Time-series friendly |
| Dev DB         | SQLite                          | Easy testing |
| API            | FastAPI                         | Fast + modern |
| Ingestion      | Python (requests + pandas)      | Rich ecosystem |
| Scheduler      | Cron / GitHub Actions / Celery  | Daily + live |
| Caching        | Redis (optional)                | Live endpoints |

---

## Data Coverage Target

- Companies & metadata
- Daily OHLCV (adjusted + unadjusted)
- Floorsheet (transaction level)
- Indices (NEPSE + sector)
- Corporate actions (dividend, rights, bonus)
- Live prices + market depth (during market hours)
- Broker activity aggregates

---

## Scaling Path

1. **Phase 1** (Now): Historical base + sample live polling
2. **Phase 2**: Daily automated EOD updates
3. **Phase 3**: Live websocket / frequent polling + caching
4. **Phase 4**: Switch critical paths to licensed feed
