"""Routes for the User entity."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.use_cases.auth.login import Login
from src.application.use_cases.auth.register import Register
from src.infrastructure.config.settings import rate_limit_settings
from src.infrastructure.database.session import get_db
from src.infrastructure.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from src.infrastructure.security.rate_limit import limiter
from src.presentation.schemas.auth import AuthResponse, LoginRequest
from src.presentation.schemas.user import CreateUserRequest

router = APIRouter(prefix="/auth")


@router.post("/singup", response_model=AuthResponse)
@limiter.limit(rate_limit_settings.auth_limit)
async def create_user(
    request: Request,
    data: CreateUserRequest,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> AuthResponse:
    """
    Register a new user.

    Arguments:
        name: str
            The name of the user.
        email: str
            The email of the user.
        password: str
            The password of the user.

    Returns:
        AuthResponse
            The output data returned after a successful authentication.
    """
    return await Register(user_repository=SQLAlchemyUserRepository(db)).execute(
        name=data.name, email=data.email, password=data.password
    )


@router.post("/singin", response_model=AuthResponse)
@limiter.limit(rate_limit_settings.auth_limit)
async def login(
    request: Request,
    data: LoginRequest,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> AuthResponse:
    """
    Login a user.

    Arguments:
        email: str
            The email of the user.
        password: str
            The password of the user.

    Returns:
        AuthResponse
            The output data returned after a successful authentication.
    """
    return await Login(user_repository=SQLAlchemyUserRepository(db)).execute(
        email=data.email, password=data.password
    )
