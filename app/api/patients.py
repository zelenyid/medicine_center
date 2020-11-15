from fastapi import APIRouter
from bson.objectid import ObjectId

from app.database.patient import PatientsCollection


router = APIRouter()


@router.get('/profile/patient/{user_id}')
async def get_patient_profile(user_id: str):
    """
    Get data for patients profile

    :param user_id: Id of user in database
    :return: patient data
    """

    doctor_data = PatientsCollection.to_json(PatientsCollection.get_one_obj({'user_id': ObjectId(user_id)}))

    return doctor_data


@router.get('/patients/')
async def get_all_patient():
    """
    Get all patients from database
    :return: list of doctors
    """
    return PatientsCollection.to_json(PatientsCollection.get_all_objects())
