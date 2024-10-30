from Car import Car
from Customer import Customer
from Motorbike import Motorbike

def display_available_vehicles(vehicles):
    brands = {}

    # Group vehicles by brand and model
    for vehicle in vehicles:
        if vehicle.is_available():  # a method to check availability
            if vehicle.make not in brands:
                brands[vehicle.make] = {}
            if vehicle.model not in brands[vehicle.make]:
                brands[vehicle.make][vehicle.model] = []
            brands[vehicle.make][vehicle.model].append(vehicle)

    # To display available vehicles grouped by brand and model
    if not brands:
        print("No vehicles are currently available.")
        return

    for brand, models in brands.items():
        print(f"\nBrand: {brand}")
        for model, vehicles in models.items():
            print(f"  Model: {model}")
            for vehicle in vehicles:
                print(f"    Number Plate: {vehicle.number_plate}")

def main():
    vehicles = []
    customers = []

    # available cars with  number plates
    vehicles.append(Car("Toyota", "Camry", 2020, 50, "KCA 001M"))
    vehicles.append(Car("Toyota", "Corolla", 2021, 40, "KCA 002M"))
    vehicles.append(Car("Toyota", "Hilux", 2019, 90, "KCA 003M"))
    vehicles.append(Motorbike("Yamaha", "YZF-R3", 2019, 30, 321, "KCA 004M"))
    vehicles.append(Motorbike("Honda", "CBR500R", 2020, 35, 500, "KCA 005M"))
    vehicles.append(Car("BMW", "X5", 2022, 100, "KCA 006M"))
    vehicles.append(Car("BMW", "3 Series", 2021, 70, "KCA 007M"))
    vehicles.append(Car("Suzuki", "Vitara", 2022, 55, "KCA 008M"))
    vehicles.append(Car("Kia", "Seltos", 2021, 65, "KCA 009M"))
    vehicles.append(Car("Nissan", "Navara", 2018, 75, "KCA 010M"))

    # Customers list
    customers.append(Customer("Alice", "DL12345"))
    customers.append(Customer("Bob", "DL67890"))
    customers.append(Customer("Sandra", "DL13579"))  

    while True:
        print("\nVehicle Rental Management System")
        print("1. Display available vehicles")
        print("2. Rent a vehicle")
        print("3. Return a vehicle")
        print("4. Display customer info")
        print("5. Add a new customer") 
        print("6. Delete a customer")    
        print("7. Update a customer")    
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_available_vehicles(vehicles)
        elif choice == "2":
            customer_name = input("Enter customer name: ")
            vehicle_number_plate = input("Enter the vehicle number plate to rent: ")
            customer = next((c for c in customers if c.name == customer_name), None)

            vehicle = next((v for v in vehicles if v.number_plate == vehicle_number_plate), None)

            if customer and vehicle and vehicle.is_available():
                customer.rent_vehicle(vehicle)
                print(f"{customer.name} has rented {vehicle.make} {vehicle.model} with number plate {vehicle.number_plate}.")
            else:
                print("Invalid customer or vehicle selection, or the vehicle is not available.")
        elif choice == "3":
            customer_name = input("Enter customer name: ")
            customer = next((c for c in customers if c.name == customer_name), None)

            if customer:
                customer.return_vehicle()
                print(f"{customer.name} has returned their vehicle.")
            else:
                print("Customer not found.")
        elif choice == "4":
            for customer in customers:
                customer.display_info()
        elif choice == "5":  
            new_customer_name = input("Enter the new customer's name: ")
            new_driver_license = input("Enter the driver's license number: ")
            new_customer = Customer(new_customer_name, new_driver_license)
            customers.append(new_customer)
            print(f"Customer {new_customer.name} added successfully.")
        elif choice == "6":  
            customer_name = input("Enter the customer's name to delete: ")
            customer = next((c for c in customers if c.name == customer_name), None)

            if customer:
                customers.remove(customer)
                print(f"Customer {customer.name} deleted successfully.")
            else:
                print("Customer not found.")
        elif choice == "7":  
            customer_name = input("Enter the customer's name to update: ")
            customer = next((c for c in customers if c.name == customer_name), None)

            if customer:
                new_name = input("Enter the new name: ")
                new_driver_license = input("Enter the new driver's license number: ")
                customer.name = new_name
                customer.driver_license = new_driver_license
                print(f"Customer {customer.name} updated successfully.")
            else:
                print("Customer not found.")
        elif choice == "8":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()