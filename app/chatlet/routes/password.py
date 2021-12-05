from fastapi import APIRouter, Body, Depends, Response
from fastapi_jwt_auth import AuthJWT
from pydantic import EmailStr

from app.chatlet.models.user import User, UserOut
from app.chatlet.util.mail import send_password_reset
from app.chatlet.util.password import hash_password

router = APIRouter(prefix='/password', tags=['Password'])


@router.post('/forgot')
async def forgot_password(
        email: EmailStr = Body(..., embed=True), auth: AuthJWT = Depends()
):
    user = await User.find_one(email == User.email)
    token = auth.create_access_token(user.email)
    await send_password_reset(email, token)
    return Response(status_code=200)


@router.post('/reset/{token}', response_model=UserOut)
async def reset_password(
        token: str, password: str = Body(..., embed=True), auth: AuthJWT = Depends()
):
    auth._token = token
    user = await User.find_one(auth.get_jwt_subject() == User.email)
    user.password = hash_password(password)
    await user.save()
    return user
