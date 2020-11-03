from fastapi.params import Depends
from fastapi_jwt_auth import AuthJWT

from app.validators.schemes.user_schemes import UserScheme
from app.database.user import User
from app.main import app
from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get('/')
def init():
    # User.insert_obj({'email': 'test', 'password': 'test'})
    return {"status": "ok", "msg": "init page"}


@router.post('/login')
async def login(user: UserScheme, Authorize: AuthJWT = Depends()):
    # subject identifier for who this token is for example id or username from database
    registered_user = User.get_one_obj({"email": user.email})
    if registered_user:
        print(registered_user)
        access_token = Authorize.create_access_token(subject=registered_user['email'])
        refresh_token = Authorize.create_refresh_token(subject=registered_user['email'])

        await app.state.redis.save_tokens(Authorize.get_jti(access_token), Authorize.get_jti(refresh_token))
        return {"access_token": access_token, "refresh_token": refresh_token}
    return {"result": False}


@router.get('/logout')
async def logout(Authorize: AuthJWT = Depends()):
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
