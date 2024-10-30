import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (EU Spec)")


if __name__ == "__main__":
    EU_Factory = EUVehicleFactory()

    eu_car = EU_Factory.create_car("Tesla", "Model S")
    eu_car.start_engine()

    eu_motorcycle = EU_Factory.create_motorcycle("Kawasaki", "Ninja")
    eu_motorcycle.start_engine()

    US_Factory = USVehicleFactory()

    us_car = US_Factory.create_car("Toyota", "Corolla")
    us_car.start_engine()

    us_motorcycle = US_Factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_motorcycle.start_engine()
