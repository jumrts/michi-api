"""Routes for the Auth."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.use_cases.auth.login import Login
from src.application.use_cases.auth.register import Register
from src.infrastructure.config.settings import auth_settings, rate_limit_settings
from src.infrastructure.database.session import get_db
from src.infrastructure.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from src.infrastructure.security.jwt import decode_access_token
from src.infrastructure.security.rate_limit import limiter
from src.presentation.schemas.auth import LoginRequest
from src.presentation.schemas.user import CreateUserRequest, UserResponse

router = APIRouter(prefix="/auth")


@router.post("/register")
@limiter.limit(rate_limit_settings.auth_limit)
async def register(
    request: Request,
    response: Response,
    data: CreateUserRequest,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> UserResponse:
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
        UserResponse
            The user.
    """
    user = await Register(user_repository=SQLAlchemyUserRepository(db)).execute(
        name=data.name, email=data.email, password=data.password
    )
    return UserResponse(
        id=str(user.id),
        name=user.name,
        email=user.email,
    )


@router.post("/login")
@limiter.limit(rate_limit_settings.auth_limit)
async def login(
    request: Request,
    response: Response,
    data: LoginRequest,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> UserResponse:
    """
    Login a user.

    Set a cookie with the access token to
    be used in the future requests.

    Arguments:
        email: str
            The email of the user.
        password: str
            The password of the user.

    Returns:
        UserResponse
            The user.
    """
    user, token = await Login(user_repository=SQLAlchemyUserRepository(db)).execute(
        email=data.email, password=data.password
    )

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=auth_settings.cookie_secure,
        samesite="lax",
        max_age=auth_settings.expiration_seconds,
        path="/",
    )

    return UserResponse(
        id=str(user.id),
        name=user.name,
        email=user.email,
    )


@router.get("/me")
@limiter.limit(rate_limit_settings.default_limit)
async def get_me(
    request: Request,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> UserResponse:
    """
    Get the current user.

    Get the cookie from the request and decode it to get the user ID.
    Then get the user from the database using the user ID.

    Arguments:
        request: Request
            The request object.
        db: Annotated[AsyncSession, Depends(get_db)]
            The database session.

    Returns:
        UserResponse
            The user.
    """
    token = request.cookies.get("access_token")
    if token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user_id = decode_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    repository = SQLAlchemyUserRepository(db)
    user = await repository.get_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return UserResponse(
        id=str(user.id),
        name=user.name,
        email=user.email,
    )
