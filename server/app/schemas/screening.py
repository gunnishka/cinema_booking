from datetime import datetime
from decimal import Decimal

from .base import OrmBase


class ScreeningBase(OrmBase):
    movie_id: int
    hall_id: int
    start_time: datetime
    price: Decimal


class ScreeningCreate(ScreeningBase):
    pass


class ScreeningOut(ScreeningBase):
    id: int


__all__ = ["ScreeningBase", "ScreeningCreate", "ScreeningOut"]

