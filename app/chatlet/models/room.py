import datetime
from typing import List

from pydantic import BaseModel, EmailStr
from beanie import Document

from app.chatlet.models.user import UserOut


class Message(BaseModel):
    content: str
    sent_by: EmailStr
    sent_at: datetime.datetime = datetime.datetime.now()


class Room(Document):
    theme: str
    created_at: datetime.datetime = datetime.datetime.now()
    room_name: str
    members: List[UserOut] = None
    messages: List[Message] = None
