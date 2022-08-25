important_building_coeff = 0.2


class District:
    """
        Класс, описывающий характеристики района: количество людей с ТС и без,
        жилую/нежилую площадь
    """

    def __init__(self, live_people: int, office_people: int):
        self.live_people = live_people // 35
        self.office_people = office_people // 10
        self.all_people = self.live_people + self.office_people
        self.all_auto = round(self.all_people / 1.2, 2)
        self.all_metro = self.all_people - int(self.all_auto)

    def getter(self) -> list:
        return {'auto': self.all_auto, 'metro': self.all_metro}


class Building:
    """
        Родительский класс для всех строений
        self.type - тип строения
        self.data - возращаемая информация об объекте
        self.metro_people - люди без иИТС
        self.auto - люди с ИТС
        self.distance - Расстояние
        self.work_place - Площадь, задействованная для чего-то
        self.area - Площадь объекта
        self.important_buildings - Количество влияющих на траффик строений(школ и т.п.) поблизости.
    """

    def __init__(self, area: float, floors: int,
                    distance: float, coeff: float, important_num: int):
        self.type = None
        self.metro_people = None
        self.auto = None
        self.distance = distance
        self.work_place = None
        self.area = area
        self.important_buildings = important_num
        self.number_of_floors = floors
        self.coeff = coeff * self.important_buildings

    def setter(self):
        self.work_place = (self.area * self.number_of_floors) // self.coeff
        self.auto = round(self.work_place / 1.2)
        self.metro_people = self.work_place - self.auto

    def getter(self):
        # answers [auto, metro, all_people, type, k]
        return {'auto': self.auto, 'metro': self.metro_people,
                    'work_place': self.work_place, 'type': self.type, 'coeff': self.coeff}


class Office(Building):
    def __init__(self):
        super().__init__()
        self.setter()
        self.type = "office"
        print(self.getter())


class House(Building):
    def __init__(self):
        super().__init__()
        self.setter()
        self.type = "house"


class Houses(House):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.setter()
        self.type = "houses"


class Hotel(Building):
    def __init__(self):
        super().__init__()
        self.setter()
        self.type = "hotel"


class Infrastructure:
    """
        Родительский класс всех объектов инфраструктуры
    """

    def __init__(self, max_passengers: int):
        self.using_passenger_traffic = None
        self.max_bandwidth = None
        self.max_passenger_traffic = max_passengers
        self.using_bandwidth = None
    
    def getter(self):
        return self.max_passenger_traffic, self.using_bandwidth

class Metro(Infrastructure):
    def __init__(self, max_passengers: int, metro_people: float, all_metro: float, coeff: float):
        super().__init__(max_passengers)
        self.settings()
        self.using_passenger_traffic = 0.35 * (all_metro + metro_people) * coeff
        self.using_bandwidth = {round(100 * self.using_passenger_traffic / self.max_passenger_traffic)}


class Road(Infrastructure):
    def __init__(self, max_passengers: int, auto: float, all_auto: float, coeff: float):
        super().__init__(max_passengers)
        self.settings()
        self.using_passenger_traffic = 0.35 * (auto + all_auto) * coeff
        self.using_bandwidth = round(100 * self.using_passenger_traffic / self.max_passenger_traffic)
