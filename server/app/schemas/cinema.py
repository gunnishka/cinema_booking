from typing import Optional

from .base import OrmBase


class CinemaBase(OrmBase):
    name: str
    address: Optional[str] = None


class CinemaCreate(CinemaBase):
    pass


class CinemaOut(CinemaBase):
    id: int


__all__ = ["CinemaBase", "CinemaCreate", "CinemaOut"]

