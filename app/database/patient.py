from app.database.database import MongoBase
from typing import Sequence, Tuple
from bson.objectid import ObjectId


class PatientsCollection(MongoBase):
    collection_name: str = 'patient'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'profession', 'conditions')


if __name__ == '__main__':
    # PatientsCollection.insert_obj({
    #     'user_id': ObjectId('5fb189db6fff7b02901732a2'),
    #     'profession': 'Ananas',
    #     'conditions': 'Vegetable'
    # })

    print(PatientsCollection.get_all_objects())
