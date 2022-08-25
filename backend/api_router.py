from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from algorithm import *
import aiohttp
from geopy import distance
from backend.schemas.district import DistrictData
from backend.schemas.buildings import BuildingData, HousesData

router = APIRouter(
    prefix='/api'
)
apikey = '67b62d8b-ea26-4350-a5f6-6e7a3c6ed99e'
url = 'https://geocode-maps.yandex.ru/1.x'
params = {
    'apikey': apikey,
    'geocode': None,
    'sco': 'latlong',
    'kind': 'metro',
    'format': 'json'
}
bellar_district = District(202000,212000)
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


@router.get('/traffic')
async def get_info(cords: str, type: str, area: float, floors: int, schools: int, n: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, params=params) as response:
             metro_info = await response.json()
    metro_name = metro_info['response']['GeoObjectCollection']['featureMember'][1]['GeoObject']['name']
    metro_cords = [float(i) for i in metro_info['response']['GeoObjectCollection']['featureMember'][1]['GeoObject']['Point']['pos']][::-1]
    cords = [float(i) for i in cords.split(',')]
    dst = distance.geodesic(cords, metro_cords).m
    metro_coeff = dst // 500