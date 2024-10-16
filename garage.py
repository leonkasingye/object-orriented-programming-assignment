from car import Car
from vehicle.truck import Truck

class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def setVehicle(self, parked):
        self.parked_vehicle = parked

    def toString(self):
        return f"Description of the parked vehicle:\n{self.parked_vehicle.toString()}"
