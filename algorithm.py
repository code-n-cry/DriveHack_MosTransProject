important_building_coeff = 1.2
k_high = 1


def time(tim: str):
    ans = tim.split(':')
    ans = int(ans[0]) * 60 + int(ans[1])
    return ans


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
        self.distance = None
        self.work_place = None
        self.area = area
        self.important_buildings = important_num
        self.number_of_floors = floors
        self.coeff = coeff
        self.n = n
        self.K_high = 1

    def setter(self):
        self.work_place = self.important_buildings * self.K_high * self.n * (
                self.area * self.number_of_floors) // self.coeff
        self.auto = round(self.work_place / 1.3)
        self.metro_people = self.work_place - self.auto

    def getter(self):
        # answers [auto, metro, all_people, type, k]
        return {'auto': self.auto, 'metro': self.metro_people,
                'work_place': self.work_place, 'type': self.type, 'coeff': self.coeff}


class Office(Building):
    def __init__(self, area: float, floors: int,
                 distance: float, important_num: int, n: int):
        super().__init__(area, floors, distance, 10, important_num, 1)
        self.distance = distance
        if self.distance >=3500:
            self.K_high = 1
        elif self.distance <= 500:
            self.K_high = 1
        elif 500 < self.distance <= 1000:
            self.K_high = 0.3
        else:
            self.K_high = 0.2
        self.setter()
        self.type = "office"


class House(Building):
    def __init__(self, area: float, floors: int,
                 distance: float, important_num: int, n: int):
        super().__init__(area, floors, distance, 25, important_num, 1)
        self.n = n
        self.distance = distance
        if self.distance >= 3500:
            self.K_high = 0
            k_high = 0
        elif self.distance <= 500:
            self.K_high = 1
        elif 500 < self.distance <= 1000:
            self.K_high = 0.3
        else:
            self.K_high = 0.09
        self.setter()
        self.type = "house"


class Houses(House):
    def __init__(self, area: float, floors: int,
                 distance: float, important_num: int, n: int):
        super().__init__(area, floors, distance, important_num, n)
        self.n = n
        self.distance = distance
        if self.distance >=3500:
            self.K_high = 1
        elif self.distance <= 500:
            self.K_high = 1
        elif 500 < self.distance <= 1000:
            self.K_high = 0.3
        else:
            self.K_high = 0.2
        self.setter()
        self.type = "houses"


class Hotel(Building):
    def __init__(self, area: float, floors: int,
                 distance: float, important_num: int, n: int):
        super().__init__(area, floors, distance, 45, important_num, 1)
        self.n = n
        self.distance = distance
        if self.distance >=3500:
            self.K_high = 1
        elif self.distance <= 500:
            self.K_high = 1
        elif 500 < self.distance <= 1000:
            self.K_high = 0.3
        else:
            self.K_high = 0.2
        self.setter()
        self.type = "hotel"


class Infrastructure:
    """
        Родительский класс всех объектов инфраструктуры
    """

    def __init__(self, max_passengers: int, metro_people: list, all_metro: list, rush_people: float, direction: int,
                 pick: str):
        self.using_passenger_traffic = None
        self.max_bandwidth = None
        self.max_passenger_traffic = max_passengers
        self.using_bandwidth = None


class Metro(Infrastructure):
    def __init__(self, max_passengers: int, metro_people: list, all_metro: list, rush_people: float, direction: int,
                 pick: str):
        super().__init__(max_passengers, metro_people, all_metro, rush_people, direction, pick="12:30")
        self.time = time(pick)
        self.max_passengers = max_passengers
        self.rush_hour = rush_people
        self.sum_people = metro_people['metro'] + metro_people['auto']
        if (metro_people['metro']) + metro_people['auto']and k_high:
            self.using_passenger_traffic = (all_metro['metro'] + metro_people['metro']) * metro_people['coeff']
            if 360 <= self.time <= 540 or 1020 <= self.time <= 1200:
                self.rush_hour = 0.3 * 0.6 * (
                        (all_metro['metro'] + metro_people['metro']) * metro_people['coeff']) + rush_people
            else:
                self.rush_hour = 0.35 * 0.5 * (
                        (all_metro['metro'] + metro_people['metro']) * metro_people['coeff']) + rush_people
            self.percentage = round(100 * self.rush_hour / self.max_passengers, 1)

            self.effect = round(round((100 * (self.rush_hour) / self.max_passengers), 1) - round(
                10 * (self.rush_hour - rush_people) / self.max_passengers, 1), 1)
            self.house_people = (metro_people['metro']) + metro_people['auto']
            self.a = round(self.percentage - self.effect, 1)
        else:
            self.a = 0

            self.percentage =round(1000*9.6 / 18000, 1)

    def getter(self):
        if self.a and k_high:
            return [
                {'effect_inequality': self.a, 'house_people': self.sum_people},
                {'rush_hour': self.rush_hour, 'using_bandwidth': self.percentage}]
        else:
            return [
                {'effect_inequality': self.a, 'house_people': self.sum_people},
                {'rush_hour': self.rush_hour, 'using_bandwidth': self.percentage}]


class Road(Infrastructure):
    def __init__(self, max_passengers: int, auto: list, all_auto: list, rush_people: float, direction: int, pick: str):
        super().__init__(max_passengers, auto, all_auto, rush_people, pick="12:30", direction=1)
        self.max_passengers = max_passengers
        self.time = time(pick)
        self.using_passenger_traffic = (auto['auto'] + all_auto['auto']) * auto['coeff']
        if direction and 360 <= self.time <= 540:  # в центр
            self.rush_hour = round(0.45 / 24 * ((auto['auto'] + all_auto['auto']) * auto['coeff'])) + rush_people
            print(self.rush_hour)
        elif not (direction) and 360 <= self.time <= 540:
            self.rush_hour = round(0.2 / 24 * ((auto['auto'] + all_auto['auto']) * auto['coeff'])) + rush_people
            print(self.rush_hour)

        else:  # из центра
            self.rush_hour = round(0.3 / 24 * ((auto['auto'] + all_auto['auto']) * auto['coeff'])) + rush_people
        self.effect = round(round(10 * self.rush_hour / self.max_passengers, 1) - round(
            10 * (self.rush_hour - rush_people) / self.max_passengers, 1), 1)
        self.percentage = round(10 * self.rush_hour / self.max_passengers, 1)
        self.house_people = (auto['auto']) + auto['metro']

    def getter(self):

        return [{'effect_inequality': self.effect, 'house_people': round(self.house_people)},  # red color
                {'rush_hour': self.rush_hour, 'percentage of max using': self.percentage}]

# rod = Road(1562, dom.getter(), Bellar_district.getter(), 724, 1, "01:30")
# self, max_passengers: int, auto: list, all_auto: list, rush_people: float, direction: int, pick: str
