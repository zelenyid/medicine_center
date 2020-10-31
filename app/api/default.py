from app.validators.schemes.user_schemes import LoginScheme
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def init():
    return {"status": "ok", "msg": "init page"}


@router.post('/login')
async def login(request: LoginScheme):
    return {"status": "ok", "msg": "logged in"}


@router.post('/logout')
async def logout():
    return {"status": "ok", "msg": "logged out"}


@router.get('/search/{name}')
async def logout(name):
    return {"status": "ok", "msg": "logged out"}

@router.get('/{user}')
async def logout(user):
    return {"status": "ok", "msg": "logged out"}

@router.get('/{user}/{schedule}')
async def logout(user, schedule):
    return {"status": "ok", "msg": "{}'s {}".format(user, schedule)}