from .base import OrmBase


class HallBase(OrmBase):
    name: str
    cinema_id: int


class HallCreate(HallBase):
    pass


class HallOut(HallBase):
    id: int


__all__ = ["HallBase", "HallCreate", "HallOut"]

