from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def init():
    return {"status": "ok"}


@router.post('/login')
async def login():
    return {"status": "ok"}


@router.post('/logout')
async def logout():
    return {"status": "ok"}