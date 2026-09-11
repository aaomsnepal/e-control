-- NEPSE Data System Schema
-- Compatible with PostgreSQL / SQLite (minor adjustments)

-- Companies / Securities
CREATE TABLE IF NOT EXISTS companies (
    id              INTEGER PRIMARY KEY,
    symbol          TEXT UNIQUE NOT NULL,
    name            TEXT,
    sector          TEXT,
    instrument_type TEXT,          -- equity, debenture, mutual fund etc.
    listed_shares   REAL,
    is_active       BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Daily OHLCV
CREATE TABLE IF NOT EXISTS daily_prices (
    id              INTEGER PRIMARY KEY,
    symbol          TEXT NOT NULL,
    trade_date      DATE NOT NULL,
    open            REAL,
    high            REAL,
    low             REAL,
    close           REAL,
    ltp             REAL,
    volume          REAL,          -- traded quantity
    turnover        REAL,          -- traded amount
    percent_change  REAL,
    source          TEXT,          -- which source provided this row
    UNIQUE(symbol, trade_date)
);

CREATE INDEX IF NOT EXISTS idx_daily_prices_symbol_date ON daily_prices(symbol, trade_date);

-- Floorsheet (transaction level)
CREATE TABLE IF NOT EXISTS floorsheet (
    id              INTEGER PRIMARY KEY,
    trade_date      DATE NOT NULL,
    contract_no     TEXT,
    symbol          TEXT NOT NULL,
    buyer_broker    TEXT,
    seller_broker   TEXT,
    quantity        REAL,
    rate            REAL,
    amount          REAL,
    source          TEXT
);

CREATE INDEX IF NOT EXISTS idx_floorsheet_date_symbol ON floorsheet(trade_date, symbol);

-- Indices
CREATE TABLE IF NOT EXISTS indices (
    id              INTEGER PRIMARY KEY,
    index_name      TEXT NOT NULL,     -- NEPSE, Sensitive, Banking etc.
    trade_date      DATE NOT NULL,
    value           REAL,
    absolute_change REAL,
    percent_change  REAL,
    source          TEXT,
    UNIQUE(index_name, trade_date)
);

-- Ingestion status / logging
CREATE TABLE IF NOT EXISTS ingestion_log (
    id              INTEGER PRIMARY KEY,
    job_name        TEXT,
    status          TEXT,              -- success / failed / partial
    records_inserted INTEGER,
    message         TEXT,
    started_at      TIMESTAMP,
    finished_at     TIMESTAMP
);

-- Live snapshot (optional, for current market state)
CREATE TABLE IF NOT EXISTS live_snapshot (
    symbol          TEXT PRIMARY KEY,
    ltp             REAL,
    percent_change  REAL,
    volume          REAL,
    turnover        REAL,
    high            REAL,
    low             REAL,
    updated_at      TIMESTAMP
);
