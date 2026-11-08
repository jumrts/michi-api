"""The Debtor entity."""

from dataclasses import dataclass


@dataclass
class Debtor:
    """A debtor represents a person or entity that owes money to another person or entity.

    Attributes:
        name: str
            The name of the debtor.
        user_id: int
            The ID of the user who created the debtor.
        is_me: bool
            Whether the debtor is the user themselves or not.
    """

    name: str
    user_id: int
    is_me: bool = False
