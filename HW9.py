# Task 1
"""1. Создать класс TrafficLight (светофор):
        ● определить у него один атрибут color (цвет) и метод running (запуск);
        ● атрибут реализовать как приватный;
        ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
        зелёный;
        ● продолжительность первого состояния (красный) составляет 7 секунд, второго
        (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
        ● переключение между режимами должно осуществляться только в указанном порядке
        (красный, жёлтый, зелёный);
        ● проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    __light_color = 'color'

    def running(self):
        print('red')
        sleep(7)
        print('yellow')
        sleep(2)
        print('green')
        sleep(4)


t = TrafficLight()
t.running()

# Task 2
"""Реализовать класс Road (дорога).
        ● определить атрибуты: length (длина), width (ширина);
        ● значения атрибутов должны передаваться при создании экземпляра класса;
        ● атрибуты сделать защищёнными;
        ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
        ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
        дороги асфальтом, толщиной в 1 см*число см толщины полотна;
        ● проверить работу метода.
        Например: 20 м*5000 м*25 кг*5 см = 12500 т."""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._wight = width
        self.weight = 25
        self.height = 5

    def mass_calc(self):
        mass_calc = self._length * self._wight * self.weight * self.height / 100
        print(f'Macca асфальта {round(mass_calc)}т.')


r = Road(5000, 20)
r.mass_calc()


# Task 3
"""Реализовать базовый класс Worker (работник):
        ● определить атрибуты: name, surname, position (должность), income (доход);
        ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
        элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
        ● создать класс Position (должность) на базе класса Worker;
        ● в классе Position реализовать методы получения полного имени сотрудника
        (get_full_name) и дохода с учётом премии (get_total_income);
        ● проверить работу примера на реальных данных: создать экземпляры класса Position,
        передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


p = Position('Ivan', 'Ivanov', 'Manager', '100', '50')
p.get_full_name(),
p.get_total_income()

# Task 4
"""Реализуйте базовый класс Car:
        ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
        также методы: go, stop, turn(direction), которые должны сообщать, что машина
        поехала, остановилась, повернула (куда);
        ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
        ● добавьте в базовый класс метод show_speed, который должен показывать текущую
        скорость автомобиля;
        ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
        скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'turn {direction}')

    def show_speed(self, speed):
        print(f'speed = {speed}')


class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print('over speed!')
        else:
            print(speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print('over speed!')
        else:
            print(f'speed = {speed}')


class PoliceCar(Car):
    pass


car1 = TownCar('blue', 70, 'LADA', False)
print(car1.name)
car1.go()
car1.show_speed(70)
car1.turn('left')
car1.stop()


# Task 5
"""Реализовать класс Stationery (канцелярская принадлежность):
        ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
        сообщение «Запуск отрисовки»;
        ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
        ● в каждом классе реализовать переопределение метода draw. Для каждого класса
        метод должен выводить уникальное сообщение;
        ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
        экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


pen = Pen('ручкой')
pen.draw()
pencil = Pencil('карандашем')
pencil.draw()
handle = Handle('маркером')
handle.draw()
