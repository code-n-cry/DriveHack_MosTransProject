important_building_coeff = 1.2


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
                 distance: float, coeff: float, important_num: int, n=1):
        self.type = None
        self.metro_people = None
        self.auto = None
        self.distance = distance
        self.work_place = None
        self.area = area
        self.important_buildings = important_num
        self.number_of_floors = floors
        self.coeff = coeff
        self.n = n

    def setter(self):
        self.work_place = self.important_buildings * self.n * (self.area * self.number_of_floors) // self.coeff
        self.auto = round(self.work_place / 1.2)
        self.metro_people = self.work_place - self.auto

    def getter(self):
        # answers [auto, metro, all_people, type, k]
        return {'auto': self.auto, 'metro': self.metro_people,
                'work_place': self.work_place, 'type': self.type, 'coeff': self.coeff}


class Office(Building):
    def __init__(self, area: float, floors: int,
                 distance: float, coeff: float, important_num: int):
        super().__init__(area, floors, distance, 10, important_num, 1)
        self.setter()
        self.type = "office"


class House(Building):
    def __init__(self, area: float, floors: int,
                 distance: float, coeff: float, important_num: int, n: int):
        super().__init__(area, floors, distance, 25, important_num, 1)
        self.n = n
        self.setter()
        self.type = "house"


class Houses(House):
    def __init__(self, area: float, floors: int,
                 distance: float, coeff: float, important_num: int, n: int):
        super().__init__(area, floors, distance, 25, important_num, n)
        self.n = n
        self.setter()
        self.type = "houses"


class Hotel(Building):
    def __init__(self, area: float, floors: int,
                 distance: float, coeff: float, important_num: int, n: int):
        super().__init__(area, floors, distance, 45, important_num, 1)
        self.n = n
        self.setter()
        self.type = "hotel"


class Infrastructure:
    """
        Родительский класс всех объектов инфраструктуры
    """

    def __init__(self, max_passengers: int, metro_people: list, all_metro: list, rush_people: float, direction: int):
        self.using_passenger_traffic = None
        self.max_bandwidth = None
        self.max_passenger_traffic = max_passengers
        self.using_bandwidth = None


class Metro(Infrastructure):
    def __init__(self, max_passengers: int, metro_people: list, all_metro: list, rush_people: float, direction: int):
        super().__init__(max_passengers, metro_people, all_metro, rush_people, direction=1)
        self.max_passengers = max_passengers
        self.using_passenger_traffic = (all_metro['metro'] + metro_people['metro']) * metro_people['coeff']
        self.rush_hour = 0.35 * 0.6 * (
                    (all_metro['metro'] + metro_people['metro']) * metro_people['coeff']) + rush_people
        self.percentage = round(100 * self.rush_hour / self.max_passengers, 1)

    def getter(self):
        return {'rush_hour': self.rush_hour, 'using_bandwidth': self.percentage}


class Road(Infrastructure):
    def __init__(self, max_passengers: int, auto: list, all_auto: list, rush_people: float, direction: int):
        super().__init__(max_passengers, auto, all_auto, rush_people, direction=1)
        self.max_passengers = max_passengers
        self.using_passenger_traffic = (auto['auto'] + all_auto['auto']) * auto['coeff']
        if direction:  # в центр
            self.rush_hour = round(0.40 * 0.005023 * ((auto['auto'] + all_auto['auto']) * auto['coeff'])) + rush_people
        else:  # из центра
            self.rush_hour = round(0.20 * 0.005023 * ((auto['auto'] + all_auto['auto']) * auto['coeff'])) + rush_people

        self.percentage = round(100 * self.rush_hour / self.max_passengers, 1)

    def getter(self):

        return {'rush_hour': self.rush_hour, 'percentage of max using': self.percentage}
