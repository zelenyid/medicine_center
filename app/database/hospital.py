from app.database.database import MongoBase
from typing import Sequence, Tuple


class HospitalCollection(MongoBase):
    collection_name: str = 'hospital'
    db_fields: Sequence[Tuple[str]] = ('_id', 'name', 'address', 'phone_number')


if __name__ == '__main__':
    print(HospitalCollection.get_all_objects())
