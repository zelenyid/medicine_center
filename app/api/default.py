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