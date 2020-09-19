from .database import MongoBase
from typing import Sequence, Tuple


class Patient(MongoBase):
    collection_name: str = 'patient'
    db_fields: Sequence[Tuple[str]] = ('_id', 'name', 'surname', 'address', 'phone_number')
