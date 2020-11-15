from app.database.database import MongoBase
from typing import Sequence, Tuple
from bson.objectid import ObjectId


class DoctorsCollection(MongoBase):
    collection_name: str = 'doctor'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'hospital_id', 'rating', 'positing')


if __name__ == '__main__':
    # DoctorsCollection.insert_obj({
    #     'user_id': ObjectId('5fb18899202941a87ea630a3'),
    #     'hospital_id': ObjectId('5fb17cae579548e9cb40cd0c'),
    #     'rating': '4.5',
    #     'positing': 'Just doctor'
    # })

    print(DoctorsCollection.get_all_objects())
