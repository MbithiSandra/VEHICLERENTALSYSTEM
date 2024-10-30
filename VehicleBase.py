from abc import ABC, abstractmethod

class VehicleBase(ABC):
    @abstractmethod
    def rent(self):
        pass

    @abstractmethod
    def return_vehicle(self):
        pass

    @abstractmethod
    def display_info(self):
        pass
