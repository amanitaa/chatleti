import datetime

from beanie import Document
from pydantic import EmailStr, BaseModel


class PersonalMessage(Document):
    sender: EmailStr
    receiver: EmailStr
    sent_at: datetime.datetime = datetime.datetime.now()
    message: str
