
import motor.motor_asyncio

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from beanie import init_beanie
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from app import router
from app.chatlet.models.user import User
from .config import CONFIG
from . import config


def get_app():
    application = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)
    application.include_router(router)
    return application


app = get_app()


@AuthJWT.load_config
def get_config():
    return CONFIG


@app.exception_handler(AuthJWTException)
def jwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.on_event('startup')
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient(CONFIG.db_url)
    await init_beanie(database=client[str(CONFIG.db_name)], document_models=[User])
