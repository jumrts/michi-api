"""The Settlement model."""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base
from src.infrastructure.database.models.debtor import DebtorModel

if TYPE_CHECKING:
    from src.infrastructure.database.models.user import UserModel


class SettlementModel(Base):
    """
    The Settlement model.

    Attributes:
        id: Mapped[int]
            The ID of the settlement.
        user_id: Mapped[int]
            The ID of the user who created the settlement.
        debtor_id: Mapped[int]
            The ID of the debtor associated with the settlement.
        period: Mapped[datetime]
            The period for which the settlement is valid.
        amount: Mapped[float]
            The amount of the settlement.
        received: Mapped[datetime]
            The date and time the settlement was received.
    """

    __tablename__ = "settlements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    debtor_id: Mapped[int] = mapped_column(ForeignKey("debtors.id"))
    period: Mapped[datetime]
    amount: Mapped[float]
    received: Mapped[datetime] = mapped_column(server_default=func.now())

    user: Mapped["UserModel"] = relationship(
        back_populates="settlements",
    )

    debtor: Mapped["DebtorModel"] = relationship(
        back_populates="settlements",
    )
