from motor.motor_asyncio import AsyncIOMotorClient

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie

from app import router
from app.chatlet.models.room import Room
from app.chatlet.models.user import User
from .config import CONFIG
from . import config


def get_app() -> FastAPI:
    application = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)
    application.include_router(router)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @application.on_event("startup")
    async def init_database() -> None:
        client = AsyncIOMotorClient(CONFIG.db_url)
        await init_beanie(database=client[str(CONFIG.db_name)], document_models=[User, Room])

    return application


app = get_app()
