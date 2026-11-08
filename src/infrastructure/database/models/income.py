"""The Income model."""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models.user import UserModel


class IncomeModel(Base):
    """The Income model.

    Attributes:
        id: Mapped[int]
            The ID of the income.
        user_id: Mapped[int]
            The ID of the user who created the income.
        description: Mapped[str]
            The description of the income.
        amount: Mapped[float]
            The amount of the income.
        period: Mapped[datetime]
            The period for which the income is valid.
    """

    __tablename__ = "incomes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    description: Mapped[str]
    amount: Mapped[float]
    period: Mapped[datetime]

    user: Mapped["UserModel"] = relationship(
        back_populates="incomes",
    )
