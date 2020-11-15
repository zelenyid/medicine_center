from fastapi import APIRouter
from bson.objectid import ObjectId

from app.database.doctor import DoctorsCollection
from app.database.users import UsersCollection


router = APIRouter()


@router.get('/profile/doctor/{doctor_id}')
async def get_doctor_profile(user_id: str):
    """
    Get data for doctor's profile

    :param user_id: Id of doctor in database
    :return: doctor data
    """
    user_data = UsersCollection.to_json(UsersCollection.get_one_obj({'_id': ObjectId(user_id)}))
    doctor_data = DoctorsCollection.to_json(DoctorsCollection.get_one_obj({'user_id': ObjectId(user_id)}))

    return {**doctor_data, **user_data}


@router.get('/doctors/')
async def get_all_doctors():
    """
    Get all doctors from database
    :return: list of doctors
    """

    list_doctors = DoctorsCollection.to_json(DoctorsCollection.get_all_objects())

    for i in range(len(list_doctors)):
        user_data = UsersCollection.to_json(UsersCollection.get_one_obj({'_id': ObjectId(list_doctors[i]['user_id'])}))
        list_doctors[i] = {**list_doctors[i], **user_data}

    return list_doctors
