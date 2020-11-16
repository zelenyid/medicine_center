from fastapi import APIRouter
from bson.objectid import ObjectId

from app.database.hospital import HospitalCollection
from app.database.doctor import DoctorsCollection


router = APIRouter()


@router.get('/hospital/{hospital_id}')
async def get_hospital_profile(hospital_id: str):
    """
    Get data for hospital profile

    """
    hospital_data = HospitalCollection.to_json(HospitalCollection.get_one_obj({'_id': ObjectId(hospital_id)}))

    return hospital_data


@router.get('/hospitals')
async def get_all_hospitals():
    """
    Get all hospitals from database
    :return: list of hospitals
    """

    return HospitalCollection.to_json(HospitalCollection.get_all_objects())


@router.get('/hospital/{hospital_id}/doctors/')
async def get_hospitals_doctors(hospital_id: str):
    """
    Get doctors of hospital with hospital_id
    :param hospital_id: hospital's id
    :return: list of doctors
    """
    return DoctorsCollection.get_objs({'hospital_id': ObjectId(hospital_id)})
