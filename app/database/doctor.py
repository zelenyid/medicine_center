from app.database.database import MongoBase
from typing import Sequence, Tuple
from bson.objectid import ObjectId
from bson.errors import InvalidId


class DoctorsCollection(MongoBase):
    collection_name: str = 'doctor'
    db_fields: Sequence[Tuple[str]] = ('_id', 'user_id', 'hospital_id', 'rating', 'positing')

    @classmethod
    def get_one_obj(cls, filter, projection=None):
        try:
            filter['user_id'] = ObjectId(filter['user_id'])
        except InvalidId:
            return {'data': {}, 'description': 'Invalid id. Can\'t convert to ObjectId', 'result': False}

        return {'data': cls.to_json(cls.collection.find_one(filter, projection=projection)), 'result': True}

    @classmethod
    def get_objs(cls, filter, fields=db_fields, projection=None):
        try:
            filter['hospital_id'] = ObjectId(filter['hospital_id'])
        except InvalidId:
            return {'data': {}, 'description': 'Invalid id. Can\'t convert to ObjectId', 'result': False}

        res = list(cls.collection.find(filter, projection=projection))
        res = cls.to_json(res)

        return res


if __name__ == '__main__':
    # DoctorsCollection.insert_obj({
    #     'user_id': ObjectId('5fb18899202941a87ea630a3'),
    #     'hospital_id': ObjectId('5fb17cae579548e9cb40cd0c'),
    #     'rating': '4.5',
    #     'positing': 'Just doctor'
    # })

    print(DoctorsCollection.get_all_objects())
