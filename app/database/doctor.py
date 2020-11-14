from .database import MongoBase
from typing import Sequence, Tuple


class DoctorsCollection(MongoBase):
    collection_name: str = 'doctors'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'rating', 'position', 'hospital_id')
