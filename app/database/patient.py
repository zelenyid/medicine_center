from app.database.database import MongoBase
from typing import Sequence, Tuple
from bson.objectid import ObjectId
from bson.errors import InvalidId


class PatientsCollection(MongoBase):
    collection_name: str = 'patient'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'profession', 'conditions')

    @classmethod
    def get_one_obj(cls, filter, projection=None):
        try:
            filter['user_id'] = ObjectId(filter['user_id'])
        except InvalidId:
            return {'data': {}, 'description': 'Invalid id. Can\'t convert to ObjectId', 'result': False}

        return {'data': cls.to_json(cls.collection.find_one(filter, projection=projection)), 'result': True}


if __name__ == '__main__':
    # PatientsCollection.insert_obj({
    #     'user_id': ObjectId('5fb189db6fff7b02901732a2'),
    #     'profession': 'Ananas',
    #     'conditions': 'Vegetable'
    # })

    print(PatientsCollection.get_all_objects())
