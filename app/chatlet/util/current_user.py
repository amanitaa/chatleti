from fastapi import Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from app.chatlet.models.user import User


async def get_current_user(auth: AuthJWT = Depends()) -> User:
    auth.jwt_required()
    user = await User.by_email(auth.get_jwt_subject())
    if user is None:
        raise HTTPException(404, 'user not found')
    return user
