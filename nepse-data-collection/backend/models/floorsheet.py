"""
Floor Sheet Model

Represents transaction-level market data.
"""

from datetime import datetime


class FloorSheet:
    """Floor sheet transaction model."""
    
    def __init__(
        self,
        transaction_id: str,
        symbol: str,
        price: float,
        quantity: int,
        timestamp: datetime,
        buyer: str = None,
        seller: str = None,
    ):
        self.transaction_id = transaction_id
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp
        self.buyer = buyer
        self.seller = seller
    
    def __repr__(self):
        return (
            f"FloorSheet(id={self.transaction_id}, symbol={self.symbol}, "
            f"price={self.price}, qty={self.quantity})"
        )
