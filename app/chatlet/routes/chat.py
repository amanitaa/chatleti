from typing import List

from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from app.chatlet.models.room import Room

router = APIRouter(prefix='/chat', tags=['Chat'])


@router.post('/create-chat', response_model=Room)
async def create_chat(room: Room, auth: AuthJWT = Depends()):
    auth.jwt_required()
    await room.save()
    return room


@router.get('/get', response_model=List[Room])
async def get_chat():
    return await Room.find_all().to_list()
