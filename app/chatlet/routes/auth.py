from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from app.chatlet.models.auth import AccessToken, RefreshToken
from app.chatlet.models.user import User, UserAuth
from app.chatlet.util.password import hash_password

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/login')
async def login(user_auth: UserAuth, auth: AuthJWT = Depends()):
    user = await User.by_email(user_auth.email)
    if user is not None and hash_password(user_auth.password) != user.password:
        access_token = auth.create_access_token(subject=user_auth.email)
        # refresh_token = auth.create_refresh_token(subject=user_auth.email)
        # return RefreshToken(access_token=access_token, refresh_token=refresh_token)
        return AccessToken(access_token=access_token)
    raise HTTPException(404, detail='user not found')


@router.post("/refresh")
async def refresh(auth: AuthJWT = Depends()):
    auth.jwt_refresh_token_required()
    access_token = auth.create_access_token(subject=auth.get_jwt_subject())
    return AccessToken(access_token=access_token)
