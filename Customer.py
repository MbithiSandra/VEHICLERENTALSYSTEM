class Customer:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
        self.rented_vehicle = None

    def rent_vehicle(self, vehicle):
        if vehicle.is_available():
            vehicle.rent()
            self.rented_vehicle = vehicle
            print(f"{self.name} has rented the vehicle.")
        else:
            print("Vehicle is not available for rent.")

    def return_vehicle(self):
        if self.rented_vehicle:
            self.rented_vehicle.return_vehicle()
            print(f"{self.name} has returned the vehicle.")
            self.rented_vehicle = None
        else:
            print("No vehicle to return.")

    def display_info(self):
        vehicle_info = f"Rented vehicle: {self.rented_vehicle.make} {self.rented_vehicle.model}" if self.rented_vehicle else "No rented vehicle"
        print(f"Customer: {self.name}, License: {self.license_number}, {vehicle_info}")
