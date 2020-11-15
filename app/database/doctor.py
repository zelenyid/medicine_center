from app.database.database import MongoBase
from typing import Sequence, Tuple
from bson.objectid import ObjectId


class DoctorsCollection(MongoBase):
    collection_name: str = 'doctor'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'hospital_id', 'rating', 'positing')


# if __name__ == '__main__':
#     print(DoctorsCollection.get_all_objects())
