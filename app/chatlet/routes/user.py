from fastapi import APIRouter, Depends, Response
from fastapi_jwt_auth import AuthJWT

from app.chatlet.models.user import User, UserUpdate, UserOut
from app.chatlet.util.current_user import get_current_user

router = APIRouter(prefix='/user', tags=['User'])


@router.get('', response_model=UserOut)
async def get_user(user: User = Depends(get_current_user)):
    return user


@router.patch('', response_model=UserOut)
async def update_user(update: UserUpdate, user: User = Depends(get_current_user)):
    await user.update(**update)
    await user.save()


@router.delete('')
async def delete_user(auth: AuthJWT = Depends()):
    auth.jwt_required()
    await User.find_one(User.email == auth.get_jwt_subject()).delete()
    return Response(status_code=200)
