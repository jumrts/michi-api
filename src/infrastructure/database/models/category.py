"""The Category model."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models.user import UserModel


class CategoryModel(Base):
    """The Category model.

    Attributes:
        id: Mapped[int]
            The ID of the category.
        name: Mapped[str]
            The name of the category.
        user_id: Mapped[int]
            The ID of the user who created the category.
    """

    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["UserModel"] = relationship(back_populates="categories")
