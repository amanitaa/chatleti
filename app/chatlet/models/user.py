from datetime import datetime
from typing import Optional

from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr


class UserAuth(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]


class UserOut(BaseModel):
    email: Indexed(EmailStr, unique=True)


class User(Document, UserOut):
    password: str

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def created(self) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_email(cls, email: str) -> "User":
        return await cls.find_one(cls.email == email)
