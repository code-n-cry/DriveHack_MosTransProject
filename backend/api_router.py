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
bellar_district = District(202000, 212000)
# 0.85 - 500 - 1000
roads = {'Center': ([55.775503, 37.571737],  [55.773229, 37.554314], [55.772581, 37.572870], [55.775097, 37.582827]),
         'Out': ([55.774584, 37.560923], [55.770859, 37.567703], [55.773887, 37.579179])}
types = {'ЖК': Houses, 'Жилое': House, 'Отель': Hotel, 'Офис': Office}
metro_cords = {'Белорусская': (55.777349, 37.581997), 'Беговая': (55.773106, 37.549837)}


@router.get('/traffic')
async def get_info(cords: str, type: str, area: float, floors: int, schools: int, n: int, metro: str, time: str):
    cords = tuple(float(i) for i in cords.split(','))
    dst = distance.geodesic(cords, metro_cords[metro]).m
    print(dst)
    building = types[type](area, floors, dst, schools, n)
    metro_params = {'Default': {'Белорусская': 18000, 'Беговая': 13500}, 'Rush': {'Белорусская': 9.6, 'Беговая': 34}}
    metro = Metro(metro_params['Default'][metro], building.getter(), bellar_district.getter(), metro_params['Rush'][metro], 1, time)
    return metro.getter()
