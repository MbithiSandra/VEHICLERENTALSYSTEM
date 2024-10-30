from Vehicle import Vehicle  


class Car(Vehicle):
    def __init__(self, make, model, year, rental_rate, number_plate):
        super().__init__(make, model, year, rental_rate, number_plate)

    def display_info(self):
        super().display_info()

