# Vehicle Management System using Object-Oriented Programming

# Base class for all vehicles
class Vehicle:
    def __init__(self, make, model, year, vehicle_id):
        self.make = make
        self.model = model
        self.year = year
        self._vehicle_id = vehicle_id  # Protected attribute

    def display_info(self):
        return f"Vehicle ID: {self._vehicle_id}, Make: {self.make}, Model: {self.model}, Year: {self.year}"

# Derived class for Cars
class Car(Vehicle):
    def __init__(self, make, model, year, vehicle_id, doors):
        super().__init__(make, model, year, vehicle_id)
        self.doors = doors

    def display_info(self):
        return super().display_info() + f", Doors: {self.doors}"

# Derived class for Trucks
class Truck(Vehicle):
    def __init__(self, make, model, year, vehicle_id, cargo_capacity):
        super().__init__(make, model, year, vehicle_id)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return super().display_info() + f", Cargo Capacity: {self.cargo_capacity}kg"

# Derived class for Motorcycles
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, vehicle_id, has_sidecar):
        super().__init__(make, model, year, vehicle_id)
        self.has_sidecar = has_sidecar

    def display_info(self):
        sidecar_status = "with sidecar" if self.has_sidecar else "no sidecar"
        return super().display_info() + f", Sidecar: {sidecar_status}"

# Example usage
car = Car("Toyota", "Corolla", 2021, 101, 4)
truck = Truck("Ford", "F-150", 2020, 102, 5000)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, 103, False)

print(car.display_info())
print(truck.display_info())
print(motorcycle.display_info())
