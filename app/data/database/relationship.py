from app.data.database.database import MongoBase
from typing import Sequence, Tuple


class RelationshipCollection(MongoBase):
    collection_name: str = 'relationship'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'relative_id')
