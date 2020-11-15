from app.database.database import MongoBase
from typing import Sequence, Tuple


class HistoriesCollection(MongoBase):
    collection_name: str = 'histories'
    db_fields: Sequence[Tuple[str]] = (
        '_id', 'author_id', 'patient_id', 'title', 'date_updated', 'date_created', 'diagnosis', 'status', 'content',
        'file_name')

    @classmethod
    def get_one_obj(cls, filter, projection=None):
        res = cls.collection.find_one(filter, projection=projection)

        return cls.to_json(res)

    @classmethod
    def get_objs(cls, filter, fields=db_fields, projection=None):
        res = list(cls.collection.find(filter, projection=projection))
        res = cls.to_json(res)

        return res


if __name__ == '__main__':
    print(HistoriesCollection.get_all_objects())
