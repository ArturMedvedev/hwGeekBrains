'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

import random  # Для одной из версий метода поворота автомобиля


class Car:  # Создаем класс
    def __init__(self, speed, color, name, is_police):  # Определяем атрибуты
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):  # Метод "машина поехала"
        print(f'{self.name} is driving')

    def stop(self):  # Метод "машина остановилась"
        print(f'{self.name} is stoped')

    # def turn(self): # Метод "поворота машины"
    #     print(f'{self.name} is turning', random.choice(['right', 'left']))

    def turn(self, direction):  # Метод "поворота машины"
        print(f'{self.name} is turning {direction}')

    def show_speed(self):  # Метод проверки скорости
        print(f'{self.name}`s speed is {self.speed}')


class TownCar(Car):  # Дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):  # Переопределяем метод проверки скорости
        print(f'{self.name}`s speed is {self.speed}')
        if self.speed > 60:
            print('Over speed!')


class SportCar(Car):  # Дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):  # Дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):  # Переопределяем метод проверки скорости
        print(f'your speed is {self.speed}')
        if self.speed > 40:
            print('Over speed!')


class PoliceCar(Car):  # Дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car_1 = TownCar(80, 'black', 'camry', False)  # Экземпляр класса
# Проверяем работу методов
town_car_1.go()
town_car_1.stop()
town_car_1.turn('right')
town_car_1.show_speed()

sport_car_1 = SportCar(280, 'yellow', 'aventador', False)  # Экземпляр класса
# Проверяем работу методов
sport_car_1.go()
sport_car_1.stop()
sport_car_1.turn('left')
sport_car_1.show_speed()

work_car_1 = WorkCar(60, 'white', 'sprinter', False)  # Экземпляр класса
# Проверяем работу методов
work_car_1.go()
work_car_1.stop()
work_car_1.turn('left')
work_car_1.show_speed()

police_car_1 = PoliceCar(160, 'white', 'focus', True)  # Экземпляр класса
# Проверяем работу методов
police_car_1.go()
police_car_1.stop()
police_car_1.turn('left')
police_car_1.show_speed()

# Проверяем доступ к атрибутам
print(town_car_1.name)
print(police_car_1.is_police)
print(work_car_1.color)
print(sport_car_1.speed)
