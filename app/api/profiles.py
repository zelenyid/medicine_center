from fastapi import APIRouter

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


@router.get('/hospital/{hospital_id}')
async def get_hospital_profile(hospital_id: int):
    """
    Get data for hospital profile
    
    """
    hospital_data = HospitalCollection.get_one_obj({'user_id': str(hospital_id)})
    hospital_data.pop('_id')

    return hospital_data
