
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч'


class SportCar(Car):

    def __init__(self,  speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class TownCar(Car):
    def __init__(self,  speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль {self.name} превышает скорость!!! Скорость {self.speed} км/ч'
        return f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч'


class WorkCar(Car):
    def __init__(self,  speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль {self.name} превышает скорость!!! Скорость {self.speed} км/ч'
        return f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self,  speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        return f'{self.name} это гражданская машина'


porshe_911gt = SportCar(250, 'Жёлтый', 'Porshe 911 GT', False)
reno_logan = TownCar(39, 'Чёрный', 'Reno Logan', False)
vw_polo = WorkCar(80, 'Серый', 'VW Polo', True)
shkoda_oktavia = PoliceCar(150, 'Белый',  'Skoda Oktavia', True)
print(vw_polo.turn_left())
print(f'Машина {reno_logan.turn_right()}, машина {porshe_911gt.stop()}')
print(f'Машина {vw_polo.go()}, {vw_polo.show_speed()}')
print(f'{vw_polo.name} - {vw_polo.color}')
print(f'{porshe_911gt.name} полицейская машина? {porshe_911gt.is_police}')
print(f'{vw_polo.name} полицейская машина? {vw_polo.is_police}')
print(porshe_911gt.show_speed())
print(reno_logan.show_speed())
print(shkoda_oktavia.police())
print(shkoda_oktavia.show_speed())
