from .database import MongoBase
from typing import Sequence, Tuple


class User(MongoBase):
    collection_name: str = 'user'
    db_fields: Sequence[Tuple[str]] = ('_id', 'email', 'password')
