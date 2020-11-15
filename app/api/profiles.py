import json
import shutil
import uuid
import os

from fastapi import APIRouter, File, UploadFile

# add correct db classes. create if don't exist
# from app.validators.schemes.user_schemes import DiseaseHistoryScheme
# from app.disease_storage.upload_file import FileUploader
from app.database.doctor import DoctorCollection
from app.database.patient import PatientCollection
from app.database.hospital import HospitalCollection


router = APIRouter()

# @router.get('/add_doctor')
# async def add_doctor(user_id, name, surname, address, phone_number):
#     """
#     TEST. Adding users to db
#     """
#     print(DoctorCollection.get_all_objects())
#     response = DoctorCollection.insert_obj({'user_id':user_id, 'name':name, 'surname':surname, 'address':address, 'phone_number':phone_number})
    
#     print(response)
#     return response

@router.get('/profile/doctor/{doctor_id}')
async def get_doctor_profile(doctor_id: int):
    """
    Get data for doctor's profile
    
    :param doctor_id:
    :return: doctor data
    """
    
    doctor_data = DoctorCollection.get_one_obj({'user_id': str(doctor_id)})
    doctor_data.pop('_id')

    return doctor_data


@router.get('/profile/patient/{patient_id}')
async def get_patient_profile(patient_id: int):
    """
    Get data for patient's profile
    TODO: load data from database
    :param patient_id: id of patient who history we open
    :param history_id: id of history in the database
    :return: histories with history_id
    """
    patient_data = PatientCollection.get_one_obj({'user_id': str(patient_id)})
    patient_data.pop('_id')

    return patient_data

@router.get('/hospital/{hospital_id}')
async def get_hospital_profile(hospital_id: int):
    """
    Get data for hospital profile
    
    """
    hospital_data = HospitalCollection.get_one_obj({'user_id': str(hospital_id)})
    hospital_data.pop('_id')

    return hospital_data