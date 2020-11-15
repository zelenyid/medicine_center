from fastapi import APIRouter
from bson.objectid import ObjectId

from app.database.doctor import DoctorsCollection


router = APIRouter()


@router.get('/profile/doctor/{doctor_id}')
async def get_doctor_profile(user_id: str):
    """
    Get data for doctor's profile

    :param user_id: Id of doctor in database
    :return: doctor data
    """

    doctor_data = DoctorsCollection.to_json(DoctorsCollection.get_one_obj({'user_id': ObjectId(user_id)}))

    return doctor_data


@router.get('/doctors/')
async def get_all_doctors():
    """
    Get all doctors from database
    :return: list of doctors
    """
    return DoctorsCollection.to_json(DoctorsCollection.get_all_objects())
