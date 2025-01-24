

class Vehicle:

    def __init__(self, make, model, year, vehicle_id):
        self.make = make
        self.model = model
        self.year = year
        self._vehicle_id = vehicle_id

    def display_info(self):
        return f"Vehicle ID: {self._vehicle_id}, Make: {self.make}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, year, vehicle_id, doors):
        super().__init__(make, model, year, vehicle_id)
        self.doors = doors

    def display_info(self):
        return super().display_info() + f", Doors: {self.doors}"



class Truck(Vehicle):
    def __init__(self, make, model, year, vehicle_id, cargo_capacity):
        super().__init__(make, model, year, vehicle_id)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return super().display_info() + f", Cargo Capacity: {self.cargo_capacity}kg"    

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, vehicle_id, cargo_capacity, has_sidecar):

        super().__init__(make, model, year, vehicle_id)
        self.has_sidecar = has_sidecar

    def display_info(self):
        sidecar_status = "with sidecar" if self.has_sidecar else "no sidecar"
        return super().display_info() + f", Sidecar: {sidecar_status}"
           



car = Car("Toyata", "Corolla", 2021, 101, 4)


print(car.display_info())


