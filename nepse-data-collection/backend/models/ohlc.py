"""
OHLC Data Model

Represents Open, High, Low, Close price data for stocks.
"""

from datetime import datetime


class OHLCData:
    """OHLC price data model."""
    
    def __init__(
        self,
        symbol: str,
        date: datetime,
        open_price: float,
        high_price: float,
        low_price: float,
        close_price: float,
        volume: int,
        value: float,
    ):
        self.symbol = symbol
        self.date = date
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume
        self.value = value
    
    def __repr__(self):
        return (
            f"OHLCData(symbol={self.symbol}, date={self.date}, "
            f"close={self.close_price}, volume={self.volume})"
        )
