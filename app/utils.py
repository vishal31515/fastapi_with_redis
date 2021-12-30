from functools import lru_cache
from redis_storage.storage.redis import RedisClient
from app.config import settings


@lru_cache(maxsize=None)
def get_redis_client():
    return RedisClient(redis_host=settings.REDIS_HOST, redis_port=settings.REDIS_PORT)


redis_client = get_redis_client()
