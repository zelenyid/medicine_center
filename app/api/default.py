from fastapi.params import Depends
from fastapi_jwt_auth import AuthJWT
from starlette.responses import FileResponse

from app.validators.schemes.user_schemes import UserScheme
from app.database.user import User
from app.main import app
from fastapi import APIRouter

from config import DEBUG_LOGIN

router = APIRouter()


@router.get('/')
def init():
    return FileResponse('./static/index.html')


@router.post('/login')
def login(user: UserScheme, Authorize: AuthJWT = Depends()):
    # TODO: Check user password
    registered_user = User.get_one_obj({"email": user.email})
    if registered_user:
        access_token = Authorize.create_access_token(subject=registered_user['email'])
        refresh_token = Authorize.create_refresh_token(subject=registered_user['email'])
        if not DEBUG_LOGIN:
            app.state.redis.save_tokens(Authorize.get_jti(access_token), Authorize.get_jti(refresh_token))
        return {"access_token": access_token, "refresh_token": refresh_token, "result": True, 'user_id': str(registered_user['_id'])}
    return {"result": False}


@router.get('/logout')
async def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    app.state.redis.revoke_tokens(Authorize.get_raw_jwt()['jti'])
    return {"status": "ok", "msg": "logged out", "result": True}


# EXAMPLE OF PROTECTED ROUTE

@router.get('/protected')
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    print(current_user)
    return {"status": "ok", "msg": f"current_user: {current_user}"}
