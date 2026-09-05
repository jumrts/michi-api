"""JWT utilities."""

from datetime import UTC, datetime, timedelta

import jwt

from src.infrastructure.config.settings import auth_settings


def create_access_token(user_id: int) -> str:
    """Create a JWT access token."""
    expires_at = datetime.now(UTC) + timedelta(
        seconds=auth_settings.expiration_seconds
    )

    payload = {
        "sub": str(user_id),
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        auth_settings.secret_key,
        algorithm=auth_settings.algorithm,
    )


def decode_access_token(token: str) -> int:
    """Decode a JWT access token."""
    payload = jwt.decode(
        token,
        auth_settings.secret_key,
        algorithms=[auth_settings.algorithm],
    )

    return int(payload["sub"])
