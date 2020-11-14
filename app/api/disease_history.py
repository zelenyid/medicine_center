import json
import shutil
import uuid
import os

from fastapi import APIRouter, File, UploadFile

from app.validators.schemes.user_schemes import DiseaseHistoryScheme
from app.disease_storage.upload_file import FileUploader

router = APIRouter()


@router.get('/{patient_id}')
async def get_disease_histories(patient_id: int):
    """
    Get list of disease histories of some user
    TODO: select only "title", "date_updated", "status" from history json
    TODO: load data from database
    :param patient_id:
    :return: list of histtories
    """
    with open('app/database/test_history.json', 'r') as f:
        all_histories = json.load(f)

    histories_patient = [history for history in all_histories if
                         history['patient_id'] == patient_id]

    return histories_patient


@router.get('/read_history/{history_id}')
async def get_history(history_id: int):
    """
    Get history of some patient with some id of history
    TODO: load data from database
    :param patient_id: id of patient who history we open
    :param history_id: id of history in the database
    :return: histories with history_id
    """
    with open('app/database/test_history.json', 'r') as f:
        all_histories = json.load(f)

    history = [history for history in all_histories if history['id'] == history_id][0]

    return history


@router.post('/disease_history/add')
async def add_history(history: DiseaseHistoryScheme):
    """
    Add to database new disease history for user
    TODO: add path to dict from loaded file in form
    TODO: add data to database
    :param history: dict of data to add to database
    :return:
    """
    return history


@router.put('/disease_history/update/{history_id}')
async def update_history(history_id: int):
    """
    Update history with id - history_id
    TODO: realize this method
    :param history_id: id of history in the database
    :return:
    """
    return {'msg': 'update history'}


@router.delete('/disease_history/delete/{history_id}')
async def delete_history(history_id: int):
    """
    Delete history with id - history_id
    TODO: realize this method
    :param history_id: id of history in the database
    :return:
    """
    return {'msg': 'delete history'}


@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    """
    upload file to google cloud storage
    :param file: file to uploading
    :return:
    """
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_filename = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]
    os.rename(file.filename, new_filename)
    shutil.move(new_filename, "app/disease_storage/")

    file_uploader = FileUploader()
    file_uploader.upload_file('app/disease_storage/'+new_filename, new_filename)

    os.remove('app/disease_storage/'+new_filename)

    return {"filename": new_filename}
