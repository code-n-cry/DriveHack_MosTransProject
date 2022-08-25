from pydantic import BaseModel

class BuildingData(BaseModel):
    area: float
    floors: int
    distance: float
    coeff: float
    important_num: int


class HousesData(BuildingData):
    n: int
