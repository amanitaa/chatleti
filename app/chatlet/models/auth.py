from datetime import timedelta

from pydantic import BaseModel


class AccessToken(BaseModel):
    access_token: str
    access_token_expires: timedelta = timedelta(minutes=15)


class RefreshToken(BaseModel):
    refresh_token: str
    refresh_token_expires: timedelta = timedelta(days=30)
