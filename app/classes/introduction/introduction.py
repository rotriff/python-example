class CarInterface:
    def start(self):
        raise NotImplemented

    def stop(self):
        raise NotImplemented

    def honk(self):
        raise NotImplemented


class Car(CarInterface):
    brand = None
    color = None

    def __init__(self, brand: str, color: str):
        self.brand = brand
        self.color = color

    def change_color(self, new_color: str):
        self.color = new_color

    def tech_review(self) -> bool:
        pass

    def start(self):
        return "car is started"


class Tesla(Car):
    TESLA_BRAND = 'Tesla'

    def __init__(self, color: str):
        super().__init__(Tesla.TESLA_BRAND, color)


def car_start(car: CarInterface):
    print(car.start())


if __name__ == "__main__":
    bmw = Car('BMW', "red")
    mercedes = Car('Mercedes', 'black')

    print(bmw.brand, bmw.color)
    print(mercedes.brand, mercedes.color)

    bmw.change_color("gray")
    bmw.tech_review()
    print(bmw.brand, bmw.color)

    car_start(bmw)

    tesla = Tesla('white')
    print(tesla.brand, tesla.color)
    tesla.change_color('brown')
    print(tesla.color)
    car_start(tesla)
