from datetime import datetime

from .base import OrmBase


class UserBase(OrmBase):
    email: str
    role: str = "client"


class UserCreate(UserBase):
    password: str


class UserLogin(OrmBase):
    email: str
    password: str


class UserOut(UserBase):
    id: int
    created_at: datetime


__all__ = ["UserBase", "UserCreate", "UserLogin", "UserOut"]

