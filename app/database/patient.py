from app.database.database import MongoBase
from typing import Sequence, Tuple


class PatientsCollection(MongoBase):
    collection_name: str = 'patient'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'birthday', 'profession', 'conditions')
