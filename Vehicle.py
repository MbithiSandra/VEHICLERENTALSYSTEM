# Vehicle.py
class Vehicle:
    def __init__(self, make, model, year, rental_rate, number_plate):
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.number_plate = number_plate
        self.__is_available = True  # Private attribute for availability

    def rent(self):
        if self.__is_available:
            self.__is_available = False
            print(f"{self.make} {self.model} has been rented.")
        else:
            print(f"{self.make} {self.model} is not available for rent.")

    def return_vehicle(self):
        self.__is_available = True
        print(f"{self.make} {self.model} has been returned.")

    def display_info(self):
        status = "Available" if self.__is_available else "Not Available"
        print(f"{self.year} {self.make} {self.model}, Rate: ${self.rental_rate}/day, "
              f"Status: {status}, Plate: {self.number_plate}")

    def is_available(self):
        return self.__is_available

    def set_availability(self, availability):
        self.__is_available = availability