import pytest
from app.classes.class_Car.class_Car import Driver
from app.classes.class_Car.class_Car import Engine
from app.classes.class_Car.class_Car import Car
from app.classes.class_Car.class_Car import Lorry
from app.classes.class_Car.class_Car import SportCar

driver_jack = Driver("Jack Sparrow", 5)
bmw_engine = Engine(200, "Bayerische Motoren Werke AG")
bmw_car = Car("BMW", "lux", 2000, driver_jack, bmw_engine)
driver_stan = Driver("Stan Pines", 10)
volkswagen_engine = Engine(150, "Volkswagen")
volkswagen_car = Lorry("Volkswagen", "Commercial", 20000, driver_stan, volkswagen_engine, 180000)
driver_annie = Driver("Anakin Skywalker", 3)
gm_engine = Engine(600, "General Motors")
chevrolet_car = SportCar("Chevrolet Corvette", "S", 1500, driver_annie, gm_engine, 340)


@pytest.mark.parametrize(
    "car, message", [(bmw_car, "BMW is started"),
                     (chevrolet_car, "Chevrolet Corvette is started"),
                     (volkswagen_car, "Volkswagen is started")]
)
def test_start(car: Car, message: str):
    assert message == car.start()


@pytest.mark.parametrize(
    "car, message", [(bmw_car, "BMW is turned off"),
                     (chevrolet_car, "Chevrolet Corvette is turned off"),
                     (volkswagen_car, "Volkswagen is turned off")]
)
def test_stop(car: Car, message: str):
    assert message == car.stop()


@pytest.mark.parametrize(
    "car, message", [(bmw_car, "BMW is turning left"),
                     (chevrolet_car, "Chevrolet Corvette is turning left"),
                     (volkswagen_car, "Volkswagen is turning left")]
)
def test_turn_left(car: Car, message: str):
    assert message == car.turn_left()


@pytest.mark.parametrize(
     "car, message", [(bmw_car, "BMW is turning right"),
                     (chevrolet_car, "Chevrolet Corvette is turning right"),
                     (volkswagen_car, "Volkswagen is turning right")]
)
def test_turn_right(car: Car, message: str):
    assert message == car.turn_right()
