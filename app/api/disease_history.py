from datetime import datetime
import json

from fastapi import APIRouter


router = APIRouter()


@router.get('/user/{patient_id}/disease_history/')
def get_disease_histories(patient_id: int):
    """
    Get list of disease histories of some user
    :param patient_id:
    :return:
    """
    return {'msg': 'List of histories of {}'.format(patient_id)}


@router.get('/user/{patient_id}/disease_history/{history_id}')
def get_history(patient_id: int, history_id: int):
    """
    Get history of some patient with some id of history
    :param patient_id: id of patient who history we open
    :param history_id: id of history in the database
    :return:
    """
    f = open('test_history.json', 'r')
    histories = json.loads(f.read())
    f.close()

    return histories[history_id]


@router.post('/disease_history/add/')
async def add_history():
    pass
