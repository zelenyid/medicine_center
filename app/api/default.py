from fastapi.params import Depends
from fastapi_jwt_auth import AuthJWT

from app.validators.schemes.user_schemes import User
from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get('/')
def init():
    return {"status": "ok", "msg": "init page"}


@router.post('/login')
def login(user: User, Authorize: AuthJWT = Depends()):
    if user.email != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.get('/logout')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    print(current_user)
    return {"status": "ok", "msg": "logged out"}


@router.get('/protected')
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    print(current_user)
    return {"status": "ok", "msg": "logged out"}
