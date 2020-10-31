import aioredis
from async_property import async_property

from app.utilities.singleton import Singleton


# TODO:
redisSettings = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'port': 6379,
    'db': 6
}


class Redis(metaclass=Singleton):

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
