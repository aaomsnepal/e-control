"""
Index Model

Represents stock market indices.
"""

from datetime import datetime


class Index:
    """Stock market index model."""
    
    def __init__(
        self,
        name: str,
        date: datetime,
        value: float,
        change_percent: float = None,
        change_points: float = None,
    ):
        self.name = name
        self.date = date
        self.value = value
        self.change_percent = change_percent
        self.change_points = change_points
    
    def __repr__(self):
        return (
            f"Index(name={self.name}, date={self.date}, "
            f"value={self.value}, change={self.change_percent}%)"
        )
