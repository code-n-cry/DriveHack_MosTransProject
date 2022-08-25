from pydantic import BaseModel


class DistrictData(BaseModel):
    living_people: int
    office_people: int
