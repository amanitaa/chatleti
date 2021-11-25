from fastapi import APIRouter, HTTPException

from app.chatlet.models.user import User, UserAuth, UserOut
from app.chatlet.util.password import hash_password

router = APIRouter(prefix='/register', tags=['Register'])


@router.post('', response_model=UserOut)
async def register_user(user_auth: UserAuth):
    user = await User.by_email(user_auth.email)
    if user is not None:
        raise HTTPException(409, 'user already exist')
    hashed_password = hash_password(user_auth.password)
    user = User(email=user_auth.email, password=hashed_password)
    await user.create()
    return user
