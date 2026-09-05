"""Password hashing utilities."""

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Hash a password.

    Arguments:
        password: str
            The password to hash.

    Returns:
        str
            The hashed password.
    """
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Password must be at most 72 bytes")

    return pwd_context.hash(password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    """
    Check if a password matches a hashed password.

    Arguments:
        plain_password: str
            The plain password to check.
        password_hash: str
            The hashed password to check.

    Returns:
        bool
            True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, password_hash)
