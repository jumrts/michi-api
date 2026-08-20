"""The Task model."""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import Base

if TYPE_CHECKING:
    from src.infrastructure.database.models.user import UserModel


class TaskModel(Base):
    """
    The Task model.

    Attributes:
        id: Mapped[int]
            The ID of the task.
        user_id: Mapped[int]
            The ID of the user who created the task.
        title: Mapped[str]
            The title of the task.
        completed: Mapped[bool]
            Whether the task is completed or not.
        due_date: Mapped[datetime | None]
            The due date of the task.
        created_at: Mapped[datetime]
            The date and time the task was created.
        updated_at: Mapped[datetime]
            The date and time the task was last updated.
    """

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    due_date: Mapped[datetime | None]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    user: Mapped["UserModel"] = relationship(
        back_populates="tasks",
    )
