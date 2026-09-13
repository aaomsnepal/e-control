# NEPSE Data Collection System

A comprehensive Python-based backend system for collecting, processing, and managing Nepal Stock Exchange (NEPSE) market data.

## Overview

This system provides automated data collection and storage capabilities for:
- **OHLC Data**: Open, High, Low, Close prices for listed companies
- **Floor Sheet**: Detailed transaction-level market data
- **Indices**: Stock market indices and their movements
- **Company Metadata**: Information about all listed companies

## Project Structure

```
nespe-data-collection/
├── backend/
│   ├── app/
│   │   └── main.py              # Main application entry point
│   ├── api/                     # API endpoints
│   ├── models/                  # Data models
│   └── services/                # Business logic services
├── config/
│   └── sources.yaml             # Data source configuration
├── data/
│   ├── ohlc/                    # OHLC price data (CSV files)
│   ├── floorsheet/              # Floor sheet transaction data
│   ├── indices/                 # Stock indices data
│   └── meta/                    # Metadata (company_list.json)
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Features

✅ Automated data collection from NEPSE
✅ Real-time and historical data storage
✅ OHLC price tracking per company
✅ Floor sheet data with transaction details
✅ Company metadata management
✅ Stock indices tracking
✅ RESTful API for data access
✅ Scalable backend architecture

## Data Modules

### OHLC Data (`data/ohlc/`)
Stores historical and current price data for each listed company:
- Date
- Open Price
- High Price
- Low Price
- Close Price
- Volume
- Value

### Floor Sheet (`data/floorsheet/`)
Transaction-level market data including:
- Transaction ID
- Symbol
- Price
- Quantity
- Time
- Buyer
- Seller

### Indices (`data/indices/`)
Stock market indices data:
- NEPSE Index
- Sensitive Index (Sectors)
- Market trends

### Metadata (`data/meta/`)
Company information:
- Stock symbols
- Company names
- Sectors
- Listing dates
- Market capitalization

## Configuration

Edit `config/sources.yaml` to configure:
- Data source endpoints
- Collection frequency
- Data retention policies
- API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aaomsnepal/e-control.git
cd nepse-data-collection
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Start the application:
```bash
python backend/app/main.py
```

## API Endpoints

### Get OHLC Data
```
GET /api/ohlc/{symbol}
```

### Get Floor Sheet
```
GET /api/floorsheet/{symbol}
```

### Get Indices
```
GET /api/indices
```

### Get Companies List
```
GET /api/companies
```

## Development

### Running Tests
```bash
pytest tests/
```

### Code Style
Follows PEP 8 guidelines. Format code using:
```bash
black .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the development team

## Roadmap

- [ ] Real-time WebSocket data streaming
- [ ] Advanced analytics and reporting
- [ ] Machine learning-based predictions
- [ ] Mobile app integration
- [ ] Docker containerization
- [ ] Kubernetes deployment configs

## Acknowledgments

- Nepal Stock Exchange (NEPSE)
- Contributors and community members
