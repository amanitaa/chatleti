import motor.motor_asyncio

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Depends
from fastapi.responses import JSONResponse
from beanie import init_beanie
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from app import router
from app.chatlet.models.room import Room
from app.chatlet.models.user import User
from app.chatlet.util.current_user import get_current_user
from .config import Settings, CONFIG
from . import config
from .connection_manager import ConnectionManager


def get_app():
    application = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)
    application.include_router(router)
    return application


app = get_app()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def jwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.on_event('startup')
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient(CONFIG.db_url)
    await init_beanie(database=client[str(CONFIG.db_name)], document_models=[User, Room])


manager = ConnectionManager()


@app.websocket('/ws/{user}')
async def ws_endpoint(websocket: WebSocket, user: User = Depends(get_current_user)):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(data, websocket)
            await manager.broadcast(f'{user} says: {data}')
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f'{user} left chat')
