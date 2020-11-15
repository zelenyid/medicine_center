from .database import MongoBase
from typing import Sequence, Tuple


class PatientCollection(MongoBase):
    collection_name: str = 'patient'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'name', 'surname', 'address', 'phone_number')