from fastapi import APIRouter
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from app.data.repository import Repository
from app.validators.schemes.relationship_sheme import RelationshipScheme

router = APIRouter()


@router.post('/relationship/add')
def add_new_relative(relative: RelationshipScheme, Authorize: AuthJWT = Depends()):
    """
    Add relative to patient

    :param relative: object of
    :return: Json of result about operation
    """
    Authorize.jwt_required()
    current_role = Repository.get_user_role_by_email(Authorize.get_jwt_subject())
    if current_role == 'doctor':
        Repository.add_relative(relative)

        return {'description': 'Success add', 'result': True}
    return {'description': 'You need to be a doctor', 'result': False}


@router.get('/relationship/get')
def get_relatives_of_patient(user_id: str, Authorize: AuthJWT = Depends()):
    """
    Get all relatives of patient
    :param user_id: user_id of patient, whose relatives we're looking
    :return:
    """
    Authorize.jwt_required()
    relatives = Repository.get_relatives(user_id)

    return {'data': relatives, 'result': bool(relatives)}
