from fastapi import APIRouter

from app.data.repository import Repository
from app.validators.schemes.relationship_sheme import RelationshipScheme

router = APIRouter()


@router.post('/relationship/add')
def add_new_relative(relative: RelationshipScheme):
    """
    Add relative to patient

    :param relative: object of
    :return: Json of result about operation
    """
    Repository.add_relative(relative)

    return {'description': 'Success add', 'result': True}


@router.get('/relationship/get')
def get_relatives_of_patient(user_id: str):
    """
    Get all relatives of patient
    :param user_id: user_id of patient, whose relatives we're looking
    :return:
    """

    relatives = Repository.get_relatives(user_id)

    return {'data': relatives, 'result': bool(relatives)}
