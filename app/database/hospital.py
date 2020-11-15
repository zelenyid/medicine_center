from .database import MongoBase
from typing import Sequence, Tuple


class HospitalCollection(MongoBase):
    collection_name: str = 'hospital'
    db_fields: Sequence[Tuple[str]] = ('_id', 'name', 'address', 'phone_number')