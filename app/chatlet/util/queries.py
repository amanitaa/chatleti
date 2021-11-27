import beanie.exceptions
from beanie import PydanticObjectId
from fastapi import HTTPException, Depends
from fastapi_jwt_auth import AuthJWT

from app.chatlet.models.room import Room
from app.chatlet.models.user import User


async def get_room(chat_id: str) -> Room:
    try:
        chat = await Room.get(PydanticObjectId(chat_id))
    except (ValueError, beanie.exceptions.DocumentNotFound):
        raise HTTPException(status_code=404, detail='chat not found')

    return chat


async def get_current_user(auth: AuthJWT = Depends()) -> User:
    auth.jwt_required()
    user = await User.by_email(auth.get_jwt_subject())
    if user is None:
        raise HTTPException(404, 'user not found')
    return user
