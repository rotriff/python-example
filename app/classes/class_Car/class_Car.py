class Driver:
    full_name: str = None
    experience: str = None

    def __init__(self, full_name: str, experience: int):
        self.full_name = full_name
        self.experience = experience

    def __str__(self):
        return f'full name = {self.full_name}, experience = {self.experience} years'


class Engine:
    power: int = None
    manufacturer: str = None

    def __init__(self, power: int, manufacturer: str):
        self.power = power
        self.manufacturer = manufacturer

    def __str__(self):
        return f'power = {self.power} horse powers, manufacturer = {self.manufacturer}'


class Car:
    brand: str = None
    car_class: str = None
    weight: int = None
    driver: Driver = None
    engine: Engine = None

    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def __str__(self):
        return f'Car brand = {self.brand}, class = {self.car_class}, weight = {self.weight} kg, ' \
               f'driver : {self.driver}, engine : {self.engine}'

    def start(self):
        return f'{self.brand} is started'

    def stop(self):
        return f'{self.brand} is turned off'

    def turn_right(self):
        return f'{self.brand} is turning right'

    def turn_left(self):
        return f'{self.brand} is turning left'


class Lorry(Car):
    carrying_capacity: int = None

    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine, carrying_capacity: int):
        super().__init__(brand, car_class, weight, driver, engine)
        self.carrying_capacity = carrying_capacity

    def __str__(self):
        return f'Car brand = {self.brand}, class = {self.car_class}, weight = {self.weight} kg, ' \
               f'driver : {self.driver}, engine : {self.engine}, carrying capacity = {self.carrying_capacity} kg'


class SportCar(Car):
    max_speed: int = None

    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine, max_speed: int):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return f'Car brand = {self.brand}, class = {self.car_class}, weight = {self.weight} kg,' \
               f' driver : {self.driver}, engine : {self.engine}, maximum speed = {self.max_speed} km/h'


if __name__ == '__main__':
    driver_jack = Driver("Jack Sparrow", 5)
    bmw_engine = Engine(200, "Bayerische Motoren Werke AG")
    bmw_car = Car("BMW", "lux", 2000, driver_jack, bmw_engine)
    driver_stan = Driver("Stan Pines", 10)
    volkswagen_engine = Engine(150, "Volkswagen")
    volkswagen_car = Lorry("Volkswagen", "Commercial", 20000, driver_stan, volkswagen_engine, 180000)
    driver_annie = Driver("Anakin Skywalker", 3)
    gm_engine = Engine(600, "General Motors")
    chevrolet_car = SportCar("Chevrolet Corvette", "S", 1500, driver_annie, gm_engine, 340)
    print(volkswagen_car)
    print(bmw_car)
    print(chevrolet_car)
    print(bmw_car.start())
