from Vehicle import Vehicle


class Motorbike(Vehicle):
    def __init__(self, make, model, year, rental_rate, engine_capacity, number_plate):
        super().__init__(make, model, year, rental_rate, number_plate)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"Engine capacity: {self.engine_capacity}cc")