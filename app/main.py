from motor.motor_asyncio import AsyncIOMotorClient

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie
from fastapi_jwt_auth.exceptions import AuthJWTException

from app import router
from app.chatlet.models.room import Room
from app.chatlet.models.user import User
from .config import CONFIG
from . import config


def get_app() -> FastAPI:
    application = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)
    application.include_router(router)
    
    application.middleware(
        CORSMiddleware,
        allow_origin=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @application.on_event("startup")
    async def init_database() -> None:
        client = AsyncIOMotorClient(CONFIG.db_url)
        await init_beanie(client=client[str(CONFIG.db_name)], document_models=[User, Room])


    @app.exception_handler(AuthJWTException)
    def jwt_exception_handler(request: Request, exc: AuthJWTException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})
    return application


app = get_app()
