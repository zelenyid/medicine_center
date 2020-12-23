from fastapi import APIRouter
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from app.data.repository import Repository

router = APIRouter()


@router.get('/profile/doctor/{user_id}')
async def get_doctor_profile(user_id: str, Authorize: AuthJWT = Depends()):
    """
    Get data for doctor's profile

    :param user_id: Id of doctor in database
    :return: doctor data
    """
    Authorize.jwt_required()
    doctor_profile = Repository.get_doctor_by_id(user_id)

    return {'data': doctor_profile, 'result': bool(doctor_profile)}


@router.post('/doctors/search/')
async def get_doctors_by_filter(filter: dict, Authorize: AuthJWT = Depends()):
    """
    Get doctors list by features for search engine.

    :param filter: dict (column:"value") of features to search for.
    :return: list of found doctors.
    """
    Authorize.jwt_required()
    list_doctors = Repository.get_doctor_by_dict(filter)

    return list_doctors


@router.get('/doctors/')
async def get_all_doctors(Authorize: AuthJWT = Depends()):
    """
    Get all doctors from database

    :return: list of doctors
    """
    Authorize.jwt_required()
    list_doctors = Repository.get_all_doctors()

    return {'data': list_doctors, 'result': bool(list_doctors)}
