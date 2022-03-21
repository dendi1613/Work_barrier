from typing import Literal
from uuid import UUID
from pydantic import BaseModel, EmailStr
# Основная схема
class SpeedsterBase(BaseModel):
    name: str
    gender: Literal["male", "female", "other/non-binary"]
    email: EmailStr
    velocity_in_kms_per_hour: float
    height_in_cm: float
    weight_in_kg: float
# Пароль никогда не должен быть возвращен в ответе.
# Для этого используется третья схема, определенная ниже.
# Проверяется только запрос на создание.
class SpeedsterCreate(SpeedsterBase):
    password: str
# default schema to return on a response
class Speedster(SpeedsterBase):
    id: UUID

    class Config:
        orm_mode = True # TL;DR; помогает связать модель со схемой