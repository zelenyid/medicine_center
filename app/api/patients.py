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
    user_data = UsersCollection.get_one_obj({'_id': user_id})['data']
    patient_data = PatientsCollection.get_one_obj({'user_id': user_id})['data']

    if not patient_data:
        return {'data': {}, 'result': False}, 200

    res = {**patient_data, **user_data}
    del res['password']

    return {'data': res, 'result': True}


@router.get('/patients/')
async def get_all_patient():
    """
    Get all patients from database
    :return: list of doctors
    """
    list_patient = PatientsCollection.get_all_objects()['data']

    if not list_patient:
        return {'data': {}, 'result': False}, 200

    for i in range(len(list_patient)):
        user_data = UsersCollection.get_one_obj({'_id': list_patient[i]['user_id']})['data']
        list_patient[i] = {**list_patient[i], **user_data}

        del list_patient[i]['password']

    return {'data': list_patient, 'result': True}
