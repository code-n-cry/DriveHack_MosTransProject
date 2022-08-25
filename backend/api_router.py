from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from algorithm import *
from backend.schemas.district import DistrictData
from backend.schemas.buildings import BuildingData, HousesData

router = APIRouter(
    prefix='/api'
)
# 0.85 - 500 - 1000


@router.post('/house/')
async def create_house(house_data: BuildingData):
    house = House(*house_data)
    return house.getter()


@router.post('/district/')
async def create_district(district_data: DistrictData):
    district = District(district_data.living_people, district_data.office_people)
    return district.getter()


@router.post('/hotel/')
async def create_hotel(hotel_data: BuildingData):
    hotel = Hotel(*hotel_data)
    return hotel.getter()


@router.post('/office/')
async def create_office(office_data: BuildingData):
    office = Office(*office_data)
    return office.getter()


@router.post('/houses/')
async def create_houses(houses_data: HousesData):
    houses = Houses(*houses_data)
    return houses.getter()


@router.get('/metro/')
async def get_metro(max_passengers: int, metro_people: float, all_metro: float, coeff: float):
    metro = Metro(max_passengers, metro_people, all_metro, coeff)
    return metro.getter()


@router.get('/road/')
async def get_road(max_passengers: int, auto: float, all_auto: float, coeff: float):
    road = Road(max_passengers, auto, all_auto, coeff)
    return road.getter()

@router.get('/district/')
async def get_cogestion():
    return {'road_1': 0.23}
