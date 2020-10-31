from fastapi import FastAPI
from app.api import auth, default

app = FastAPI()

app.include_router(default.router)
app.include_router(auth.router, prefix='/auth', tags=['auth'])
