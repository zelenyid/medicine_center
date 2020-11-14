from .database import MongoBase
from typing import Sequence, Tuple


class PatientsCollection(MongoBase):
    collection_name: str = 'patients'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'profession', 'conditions')
