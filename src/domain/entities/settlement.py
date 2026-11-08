""" "The Settlement entity."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Settlement:
    """
    A settlement represents a financial transaction between a user and a debtor.

    Attributes:
        user_id: int
            The ID of the user who created the settlement.
        debtor_id: int
            The ID of the debtor associated with the settlement.
        period: datetime
            The period for which the settlement is valid.
        amount: float
            The amount of the settlement.
        received: datetime
            The date and time the settlement was received.
    """

    user_id: int
    debtor_id: int
    period: datetime
    amount: float
    received: datetime
