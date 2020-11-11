from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from app.api import auth, default, disease_history
from app.main import app
from app.storage.token_storage import RedisTokenStorage
from config import JwtSettings


@AuthJWT.load_config
def get_config():
    return JwtSettings()


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    jti = decrypted_token['jti']
    in_redis = app.state.redis.get_token(jti)
    return in_redis == RedisTokenStorage.TOKEN_VALID_STATE


@app.on_event('startup')
def startup_event():
    app.state.redis = RedisTokenStorage()


@app.on_event('shutdown')
def shutdown_event():
    app.state.redis.close()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


app.include_router(default.router)
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(disease_history.router, prefix='/history', tags=['history'])
app.mount("/static", StaticFiles(directory="static"), name='static')
