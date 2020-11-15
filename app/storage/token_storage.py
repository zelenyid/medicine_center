from app.utilities.singleton import Singleton
import redis

from config import ACCESS_EXPIRES_DELTA, REFRESH_EXPIRES_DELTA

redisSettings = {
    # 'username': 'root',
    # 'password': None,
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0
}


class RedisTokenStorage(metaclass=Singleton):
    TOKEN_VALID_STATE = '1'

    def __init__(self):
        self._redis = redis.Redis(**redisSettings)

    def save_tokens(self, access_jti, refresh_jti):
        access_jti = self._redis.set(access_jti, RedisTokenStorage.TOKEN_VALID_STATE, ACCESS_EXPIRES_DELTA)
        refresh_jti = self._redis.set(refresh_jti, RedisTokenStorage.TOKEN_VALID_STATE, REFRESH_EXPIRES_DELTA)
        return access_jti, refresh_jti

    def get_token(self, token_jti):
        return self._redis.get(token_jti)

    def revoke_tokens(self, *tokens):
        if tokens:
            self._redis.delete(*tokens)
