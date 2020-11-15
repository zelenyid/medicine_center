from app.database.database import MongoBase
from typing import Sequence, Tuple
from bson.objectid import ObjectId


class HistoriesCollection(MongoBase):
    collection_name: str = 'histories'
    db_fields: Sequence[Tuple[str]] = (
        '_id', 'author_id', 'patient_id', 'title', 'date_updated', 'date_created', 'diagnosis', 'status', 'content',
        'file_name')

    @staticmethod
    def to_json(data_lst, fields):
        return [{key: data[key] for key in fields} for data in data_lst]

    @classmethod
    def get_one_obj(cls, filter, projection=None):
        res = cls.collection.find_one(filter, projection=projection)
        res = cls.id_to_str(res)

        return res

    @classmethod
    def get_objs(cls, filter, fields=db_fields, projection=None):
        res = list(cls.collection.find(filter, projection=projection))

        res = cls.id_to_str(res)
        res = cls.to_json(res, fields)

        return res


if __name__ == '__main__':
    print(HistoriesCollection.get_all_objects())
