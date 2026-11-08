"""The Category entity."""

from dataclasses import dataclass


@dataclass
class Category:
    """A category represent the type of debt.

    Attributes:
        name: str
            The name of the debtor.
        user_id: int
            The ID of the user who created the debtor.
    """

    name: str
    user_id: int
