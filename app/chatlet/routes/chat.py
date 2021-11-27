from typing import List

from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from app.chatlet.models.room import Room, RoomsOut
from app.chatlet.util.queries import get_room

router = APIRouter(prefix='/chat', tags=['Chat'])


@router.post('/create-chat', response_model=Room)
async def create_chat(room: Room, auth: AuthJWT = Depends()):
    auth.jwt_required()
    await room.save()
    return room


@router.get('/get', response_model=List[RoomsOut])
async def get_chat():
    return await Room.find_all().to_list()


@router.get('/get/{chat_id}', response_model=RoomsOut)
async def get_chat_by_id(chat: Room = Depends(get_room)):
    return chat
