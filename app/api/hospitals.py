from fastapi import APIRouter
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from app.data.repository import Repository

router = APIRouter()


@router.get('/hospital/{hospital_id}')
async def get_hospital_profile(hospital_id: str, Authorize: AuthJWT = Depends()):
    """
    Get data for hospital profile
    """
    Authorize.jwt_required()
    hospital_profile = Repository.get_hospital_by_id(hospital_id)

    return {'data': hospital_profile, 'result': bool(hospital_profile)}


@router.get('/hospitals')
async def get_all_hospitals(Authorize: AuthJWT = Depends()):
    """
    Get all hospitals from database
    :return: list of hospitals
    """
    Authorize.jwt_required()
    list_hospitals = Repository.get_all_hospitals()

    return {'data': list_hospitals, 'result': bool(list_hospitals)}


@router.get('/hospital/{hospital_id}/doctors/')
async def get_hospitals_doctors(hospital_id: str, Authorize: AuthJWT = Depends()):
    """
    Get doctors of hospital with hospital_id
    :param hospital_id: hospital's id
    :return: list of doctors
    """
    Authorize.jwt_required()
    list_doctors = Repository.get_doctors_by_hospital_id(hospital_id)

    return {'data': list_doctors, 'result': bool(list_doctors)}
