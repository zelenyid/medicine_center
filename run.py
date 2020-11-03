from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.api import auth, default
from app.main import app
from app.storage.token_storage import Redis
from config import JwtSettings


@AuthJWT.load_config
def get_config():
    return JwtSettings()


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    jti = AuthJWT().get_jti(decrypted_token)
    print(f"jti: {jti}")
    return app.state.redis.get_token(jti) is not None


@app.on_event('startup')
async def startup_event():
    app.state.redis = Redis()
    await app.state.redis.client


@app.on_event('shutdown')
async def shutdown_event():
    app.state.redis.close()
    await app.state.redis.wait_closed()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


app.include_router(default.router)
app.include_router(auth.router, prefix='/auth', tags=['auth'])
