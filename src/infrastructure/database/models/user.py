"""The User model."""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models.task import TaskModel


class UserModel(Base):
    """
    The User model.

    Attributes:
        id: Mapped[int]
            The ID of the user.
        name: string
            The name of the user.
        email: string
            The email of the user.
        password: string
            The password of the user.
        created_at: Mapped[datetime]
            The date and time the user was created.
        updated_at: Mapped[datetime]
            The date and time the user was last updated.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    tasks: Mapped[list["TaskModel"]] = relationship(
        back_populates="user",
    )
