from pydantic import BaseModel, ConfigDict


class OrmBase(BaseModel):
    """Базовая схема с поддержкой ORM."""

    model_config = ConfigDict(from_attributes=True)

    class Config:
        orm_mode = True


__all__ = ["OrmBase"]

