from datetime import timedelta

import aioredis
from async_property import async_property

from app.utilities.singleton import Singleton


# TODO:
from config import ACCESS_EXPIRES_DELTA, REFRESH_EXPIRES_DELTA

redisSettings = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0
}


class Redis(metaclass=Singleton):
    TOKEN_VALID_STATE = 1

    def __init__(self):
        self._session = None

    @async_property
    async def client(self):
        if self._session:
            return self._session
        redisConn = await aioredis.create_pool(
            f'redis://'
            f'{redisSettings.get("user")}:'
            f'{redisSettings.get("password")}@'
            f'{redisSettings.get("host")}:'
            f'{redisSettings.get("port")}/'
            f'{redisSettings.get("db")}',
            encoding='utf-8'
        )
        self._session = aioredis.Redis(pool_or_conn=redisConn)
        return self._session

    async def save_tokens(self, access_jti, refresh_jti):
        access_jti = await self._session.set(access_jti, Redis.TOKEN_VALID_STATE, expire=ACCESS_EXPIRES_DELTA)
        refresh_jti = await self._session.set(refresh_jti, Redis.TOKEN_VALID_STATE, expire=REFRESH_EXPIRES_DELTA)
        return access_jti, refresh_jti

    async def get_token(self, token_jti):
        return await self._session.get(token_jti)


