import redis
import os
from app.config import settings
class RedisClient:
    def __init__(self, redis_host=settings.REDIS_HOST, redis_port=6379) -> None:
        self.r = redis.Redis(host=redis_host, port=redis_port, db=0)
    def set(self, key: str, value: str) -> None:
        self.r.set(key, value)
    def get(self, key: str) -> str:
        return self.r.get(key)