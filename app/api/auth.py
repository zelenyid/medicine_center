from fastapi import APIRouter
from fastapi_jwt_auth import AuthJWT

router = APIRouter()


@router.post('/refresh')
async def refresh_tokens():
    return {"status": "ok"}

