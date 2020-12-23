from fastapi import APIRouter
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from app.data.repository import Repository

router = APIRouter()


@router.get('/profile/patient/{user_id}')
async def get_patient_profile(user_id: str, Authorize: AuthJWT = Depends()):
    """
    Get data for patients profile

    :param user_id: Id of user in database
    :return: patient data
    """
    Authorize.jwt_required()
    patient_profile = Repository.get_patient_by_id(user_id)

    return {'data': patient_profile, 'result': bool(patient_profile)}


@router.post('/patients/search/')
async def get_patients_by_filter(filter: dict, Authorize: AuthJWT = Depends()):
    """
    Get patients list by attributes for search engine.

    :param filter: dict (column:"value") of attributes to search for.
    :return: list of patients.
    """
    Authorize.jwt_required()
    current_role = Repository.get_user_role_by_email(Authorize.get_jwt_subject())
    if current_role == 'doctor':
        patients = Repository.get_patient_by_dict(filter)

        return {'data': patients, 'result': True}
    return {'description': 'You need to be a doctor', 'result': False}


@router.get('/patients/')
async def get_all_patient(Authorize: AuthJWT = Depends()):
    """
    Get all patients from database

    :return: list of patients
    """
    Authorize.jwt_required()
    list_patients = Repository.get_all_patients()

    return {'data': list_patients, 'result': bool(list_patients)}
