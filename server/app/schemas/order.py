from datetime import datetime

from .base import OrmBase


class OrderBase(OrmBase):
    user_id: int
    status: str = "created"


class OrderCreate(OrderBase):
    pass


class OrderOut(OrderBase):
    id: int
    created_at: datetime


__all__ = ["OrderBase", "OrderCreate", "OrderOut"]

