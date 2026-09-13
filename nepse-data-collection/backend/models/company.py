"""
Company Model

Represents company information and metadata.
"""

from datetime import datetime


class Company:
    """Company metadata model."""
    
    def __init__(
        self,
        symbol: str,
        name: str,
        sector: str,
        listing_date: datetime,
        market_cap: float = None,
    ):
        self.symbol = symbol
        self.name = name
        self.sector = sector
        self.listing_date = listing_date
        self.market_cap = market_cap
    
    def __repr__(self):
        return f"Company(symbol={self.symbol}, name={self.name}, sector={self.sector})"
