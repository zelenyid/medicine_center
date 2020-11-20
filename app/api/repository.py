from app.database.users import UsersCollection


class Repository:
    @classmethod
    def get_obj_by_id(cls, collection, user_id):
        """
        Get object's info by id
        :param collection:
        :param user_id: id of object
        :return: object's data
        """
        return collection.to_json(collection.get_one_obj({'_id': user_id}))

    @classmethod
    def get_all_users(cls, collection, **filter_data):
        """
        Get all user data combine user data and collection data
        :param collection: collection object
        :param filter_data: filter for data
        :param fields: fields to output
        :return: list of user's data
        """
        user_list = collection.to_json(collection.get_objs(filter_data))

        if not user_list:
            return []

        for i in range(len(user_list)):
            user_data = cls.get_obj_by_id(UsersCollection, user_list[i]['user_id'])
            user_list[i] = {**user_list[i], **user_data}
            del user_list[i]['password']

        return user_list

    @classmethod
    def get_user_profile(cls, collection, user_id):
        """
        Get all data about user by id
        :param collection: collection of user
        :param user_id: user's id
        :return: user's data
        """
        user_data = cls.get_obj_by_id(UsersCollection, user_id)
        collection_data = collection.to_json(collection.get_one_obj({'user_id': user_id}))

        if not collection_data:
            return None

        user_data = {**collection_data, **user_data}
        del user_data['password']

        return user_data

    @classmethod
    def get_all_items(cls, collection, **filter_data):
        return collection.to_json(collection.get_objs(filter_data))

    @classmethod
    def insert_obj_to_collection(cls, collection, obj):
        """
        Insert to collection new object
        :param collection: Collection name
        :param obj: New object
        :return:
        """
        collection.insert_obj(dict(obj))

    @classmethod
    def update_obj(cls, collection, obj_id, new_obj):
        if obj_id in collection.get_ids():
            collection.update_obj_by_id(obj_id, dict(new_obj))
            return 'Success update'
        else:
            return 'Can\'n found by this id'

    @classmethod
    def delete_obj(cls, collection, obj_id):
        if obj_id in collection.get_ids():
            collection.delete_obj_by_id(obj_id)
            return 'Success delete'
        return 'Can\'n found by this id'
