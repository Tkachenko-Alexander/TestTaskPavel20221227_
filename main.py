
from abc import ABC, abstractmethod

class VehicleStrategy(ABC):
    @abstractmethod
    def time_to_cover_distance(self, distance):
        pass

class OnFoot(VehicleStrategy):
    def time_to_cover_distance(self, distance):
        return distance / 5

class ByBike(VehicleStrategy):
    def time_to_cover_distance(self, distance):
        return distance / 20

class ByCar(VehicleStrategy):
    def time_to_cover_distance(self, distance):
        return distance / 60

class TimeCalculator:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate_time(self, distance):
        return self._strategy.time_to_cover_distance(distance)

distance = int(input("Enter the distance in km: "))
vehicle = input("Enter the vehicle (on foot, by bike, by car): ")

if vehicle == "on foot":
    strategy = OnFoot()
elif vehicle == "by bike":
    strategy = ByBike()
elif vehicle == "by car":
    strategy = ByCar()
else:
    raise ValueError("Invalid vehicle")

calculator = TimeCalculator(strategy)
result = calculator.calculate_time(distance)

print("The time to cover the distance is: {:.2f} hours".format(result))
