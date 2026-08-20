from slowapi import Limiter
from slowapi.util import get_remote_address

from src.infrastructure.config.settings import rate_limit_settings

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[rate_limit_settings.default_limit],
)
