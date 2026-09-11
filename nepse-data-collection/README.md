# NEPSE Data Collection System

A Python-based system for collecting, processing, and storing Nepal Stock Exchange (NEPSE) data.

## Project Structure

```
nepse-data-collection/
├── backend/
│   ├── api/              # API endpoints
│   ├── app/              # Main application
│   │   └── main.py       # Entry point
│   ├── models/           # Data models
│   └── services/         # Business logic
├── config/
│   └── sources.yaml      # Data source configuration
├── data/
│   ├── floorsheet/       # Floor sheet data
│   ├── indices/          # Market indices
│   ├── meta/             # Metadata (company lists, etc.)
│   └── ohlc/             # OHLC price data
└── requirements.txt      # Python dependencies
```

## Features

- **Data Collection**: Automated collection of NEPSE stock data
- **OHLC Data**: Open, High, Low, Close price tracking
- **Indices**: Market indices data
- **Floor Sheet**: Trading floor information
- **Company Metadata**: Company information and lists

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure data sources in `config/sources.yaml`

4. Run the application:
```bash
python -m backend.app.main
```

## Configuration

Edit `config/sources.yaml` to configure:
- Data source URLs
- Collection intervals
- Data storage settings

## Data Files

### OHLC Data
- Location: `data/ohlc/`
- Format: CSV
- Example: `ADBL_prices.csv`

### Indices
- Location: `data/indices/`
- Tracks NEPSE index movements

### Floor Sheet
- Location: `data/floorsheet/`
- Trading transaction details

### Metadata
- Location: `data/meta/`
- Contains `company_list.json` with company information

## Requirements

See `requirements.txt` for Python package dependencies.

## License

MIT
