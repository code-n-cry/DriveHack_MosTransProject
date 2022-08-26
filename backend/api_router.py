from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from algorithm import *
from math import radians, cos, sin, asin, sqrt


def get_distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return(c * r) * 1000

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
bellar_district = District(0.7*202000, 0.7*212000)
# 0.85 - 500 - 1000
roads = {'Center': ([55.775503, 37.571737],  [55.773229, 37.554314], [55.772581, 37.572870], [55.775097, 37.582827]),
         'Out': ([55.774584, 37.560923], [55.770859, 37.567703], [55.773887, 37.579179])}
types = {'ЖК': Houses, 'Жилое': House, 'Отель': Hotel, 'Офис': Office}
metro_cords = {'Белорусская': (55.777349, 37.581997), 'Беговая': (55.773106, 37.549837)}


@router.get('/traffic')
async def get_info(cords: str, type: str, area: float, floors: int, schools: int, n: int, metro: str, time: str):
    cords = tuple(float(i) for i in cords.split(','))
    dst = get_distance(metro_cords[metro][0], cords[0], metro_cords[metro][1], cords[1])
    building = types[type](area, floors, dst, schools, n)
    roads = []
    metro_params = {'Default': {'Белорусская': 18000, 'Беговая': 13500}, 'Rush': {'Белорусская': 9.6, 'Беговая': 3.4}}
    metro = Metro(metro_params['Default'][metro], building.getter(), bellar_district.getter(), metro_params['Rush'][metro], 1, time)    
    return metro.getter()

