from fastapi import APIRouter

router = APIRouter()

@router.post('/')
async def auth():
    return {"status": "ok"}


@router.post('/refresh')
async def refresh_tokens():
    return {"status": "ok"}

