# MBITHI SANDRA MINOO  
**ID:** 167253

## THE VEHICLE RENTAL MANAGEMENT SYSTEM

The Vehicle Rental Management System is a simple console application designed to handle vehicle rentals. Users can browse available vehicles, rent or return them, and manage customer records, including adding, updating, or deleting customer information. The system is organized into small, modular sections—like "vehicle" and "customer"—to streamline usage and updates as needed.

---

### System Classes and Purpose

1. **Vehicle (Base Class)**  
   Represents a general vehicle with attributes common to all types, such as:
   - `make`
   - `model`
   - `year`
   - `number plate`

   Includes methods like `is_available()` to check availability and `display_info()` to show vehicle details. The Vehicle class serves as the parent for specific vehicle types (e.g., Car, Motorbike), allowing code reuse and a standardized set of attributes.

2. **Car (Derived Class)**  
   Inherits from the Vehicle class and represents cars with additional attributes if needed, like `number_of_seats`. This class utilizes the structure provided by the Vehicle class and allows for easy management of car rentals within the system.

3. **Motorbike (Derived Class)**  
   Inherits from the Vehicle class, representing motorbikes with unique attributes (e.g., `engine_capacity`). This class adapts the Vehicle class's structure to handle motorbike-specific details and makes motorbike rentals possible, giving users a variety of vehicle options.

4. **Customer**  
   Represents a customer with details such as `name` and `driver_license`. It manages customer-specific functions like renting and returning vehicles, ensuring customers can only rent one vehicle at a time. Includes methods like `display_info()` to show customer information.

---

### System Operations (Implemented in the `main()` Function)

1. **Display Available Vehicles**  
   Lists all available vehicles by brand and model, including unique number plates, making it easy for users to view and select rental options.

2. **Rent a Vehicle**  
   Facilitates vehicle rental by linking a customer to a selected, available vehicle and marking it as unavailable once rented.

3. **Return a Vehicle**  
   Allows customers to return rented vehicles, making them available again for others.

4. **Customer Management**  
   Supports adding, updating, and deleting customer records as needed, with fields like `name` and `driver’s license`.

---

This system, with its structured class hierarchy and modular functions, provides an effective solution for vehicle rental management. The interface is straightforward, and the design allows for easy expansion, such as adding new vehicle types or rental features in the future.
