from app.data.repository import Repository

from fastapi import APIRouter
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

# add correct db classes. create if don't exist
# from app.validators.schemes.user_schemes import DiseaseHistoryScheme
from app.validators.schemes.schedule_scheme import ScheduleScheme
from app.data.database.schedule import ScheduleCollection

router = APIRouter()


@router.get('/schedule/{doctor_id}')
async def get_schedule(doctor_id: str, Authorize: AuthJWT = Depends()):
    """
    Get doctor's all schedules by id
    :param doctor_id:
    :return: schedule_data
    """
    Authorize.jwt_required()
    result = Repository.get_schedule(doctor_id)

    return result


@router.post('/schedule/add')
async def add_schedule(schedule: ScheduleScheme, Authorize: AuthJWT = Depends()):
    """
    Takes schedule, adds it to database.
    :param schedule_id: 
    :return: status
    """
    Authorize.jwt_required()
    current_role = Repository.get_user_role_by_email(Authorize.get_jwt_subject())
    if current_role == 'doctor':
        ScheduleCollection.insert_obj(dict(schedule))
        return {'description': 'Addition successful', 'result': True}
    return {'description': 'You need to be a doctor', 'result': False}


@router.delete('/schedule/delete/{schedule_id}')
async def delete_schedule(schedule_id: str, Authorize: AuthJWT = Depends()):
    """
    Delete schedule by id
    :param schedule_id: 
    :return: description and status
    """
    Authorize.jwt_required()

    current_role = Repository.get_user_role_by_email(Authorize.get_jwt_subject())
    if current_role == 'doctor':
        if schedule_id in ScheduleCollection.get_ids():
            ScheduleCollection.delete_obj_by_id(schedule_id)
            return {'description': 'Delete successful', 'result': True}
        return {'description': 'Can\'t find schedule by this id', 'result': False}
    return {'description': 'You need to be a doctor', 'result': False}


@router.put('/schedule/update/{schedule_id}')
async def update_schedule(schedule_id: str, new_schedule: ScheduleScheme, Authorize: AuthJWT = Depends()):
    """
    Update schedule by id with new schedule
    :param schedule_id: id of schedule in database
    :param new_schedule: dict of new schedule
    :return: description and status
    """
    Authorize.jwt_required()
    if schedule_id in ScheduleCollection.get_ids():
        ScheduleCollection.update_obj_by_id(schedule_id, dict(new_schedule))
        return {'description': 'Update successful', 'result': True}
    return {'description': 'Can\'t find a schedule by this id', 'result': False}
