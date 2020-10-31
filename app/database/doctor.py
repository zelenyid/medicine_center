from .database import MongoBase
from typing import Sequence, Tuple


class Doctor(MongoBase):
    collection_name: str = 'doctor'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'name', 'surname', 'address', 'phone_number')
