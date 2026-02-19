from .base import OrmBase


class TicketBase(OrmBase):
    order_id: int
    screening_id: int
    row_number: int
    seat_number: int


class TicketCreate(TicketBase):
    pass


class TicketOut(TicketBase):
    id: int


__all__ = ["TicketBase", "TicketCreate", "TicketOut"]

