import cachetools
from chainlit.config import config


jwt_session_tokens = cachetools.TTLCache(
    maxsize=8096, ttl=config.project.user_session_timeout
)
