from pydantic import BaseModel


class Infrastructure(BaseModel):
    max_passengers: int


class Metro(Infrastructure):
    metro_people: float
    all_metro: float
    coeff: float


class Road(Infrastructure):
    auto: float
    all_auto: float
    coeff: float