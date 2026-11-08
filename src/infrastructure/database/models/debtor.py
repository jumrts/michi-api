"""The Debtor model."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base
from src.infrastructure.database.models.settlement import SettlementModel

if TYPE_CHECKING:
    from src.infrastructure.database.models.user import UserModel


class DebtorModel(Base):
    """ "The Debtor model.

    Attributes:
        id: Mapped[int]
            The ID of the debtor.
        name: Mapped[str]
            The name of the debtor.
        user_id: Mapped[int]
            The ID of the user who created the debtor.
        is_me: Mapped[bool]
            Whether the debtor is the user or not.
    """

    __tablename__ = "debtors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    is_me: Mapped[bool] = mapped_column(default=False)

    user: Mapped["UserModel"] = relationship(
        back_populates="debtors",
    )

    settlements: Mapped[list["SettlementModel"]] = relationship(
        back_populates="debtor",
    )
