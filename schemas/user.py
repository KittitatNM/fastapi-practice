from typing import Any, Generic, TypeVar
from pydantic import BaseModel
from datetime import datetime


class UserLogin(BaseModel):
    userId: int
    userName: str
    userPassword: str
    # userTimestamp: datetime


class UserInfo(BaseModel):
    userId: int
    userName: str
    userSurname: str


T = TypeVar("T")


class ResponseMessage():
    # responseMessage: UserInfo
    # def __init__(self, responseMessage: UserInfo):
    #     self.responseMessage = responseMessage

    def __init__(self, res: UserLogin):
        self.responseMessage = res
