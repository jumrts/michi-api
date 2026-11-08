"""The Income entity."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Income:
    """An income represents a financial transaction that increases the user's wealth.

    Attributes:
        user_id: int
            The ID of the user who created the income.
        description: str
            The description of the income.
        amount: float
            The amount of the income.
        period: datetime
            The period for which the income is valid.
    """

    user_id: int
    description: str
    amount: float
    period: datetime
