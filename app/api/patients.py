from fastapi import APIRouter
from bson.objectid import ObjectId

from app.database.patient import PatientsCollection
from app.database.users import UsersCollection


router = APIRouter()


@router.get('/profile/patient/{user_id}')
async def get_patient_profile(user_id: str):
    """
    Get data for patients profile

    :param user_id: Id of user in database
    :return: patient data
    """
    user_data = UsersCollection.to_json(UsersCollection.get_one_obj({'_id': ObjectId(user_id)}))
    patient_data = PatientsCollection.to_json(PatientsCollection.get_one_obj({'user_id': ObjectId(user_id)}))

    if not patient_data:
        return {'data': {}, 'result': False}, 200

    return {**patient_data, **user_data}


@router.get('/patients/')
async def get_all_patient():
    """
    Get all patients from database
    :return: list of doctors
    """
    list_patient = PatientsCollection.to_json(PatientsCollection.get_all_objects())

    if not list_patient:
        return {'data': {}, 'result': False}, 200

    for i in range(len(list_patient)):
        user_data = UsersCollection.to_json(UsersCollection.get_one_obj({'_id': ObjectId(list_patient[i]['user_id'])}))
        list_patient[i] = {**list_patient[i], **user_data}

    return list_patient
