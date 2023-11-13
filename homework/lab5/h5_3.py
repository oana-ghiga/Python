class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def mileage(self, distance, fuel_consumed):
        pass

    def towing_capacity(self):
        pass

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def mileage(self, distance, fuel_consumed):
        if fuel_consumed == 0:
            return 0
        return distance / fuel_consumed


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def mileage(self, distance, fuel_consumed):
        if fuel_consumed == 0:
            return 0
        return distance / fuel_consumed


class Truck(Vehicle):
    def __init__(self, make, model, year, curb_weight, gcvwr):
        super().__init__(make, model, year)
        self.curb_weight = curb_weight
        self.gcvwr = gcvwr
#To find the truck's towing capacity, subtract your truck's curb weight from its Gross Combined Vehicle Weight Rating.
    def towing_capacity(self):
        return self.gcvwr - self.curb_weight


# Example usage
car = Car("Chevrolet", "Impala", 1967)
print(car, car.mileage(500, 20))

motorcycle = Motorcycle("Kawasaki", "Ninja", 2018)
print(motorcycle, "Mileage:", motorcycle.mileage(300, 15))

truck = Truck("Jeep", "Gladiator", 2024, 5050, 6250)
print(truck, "Towing capacity:", truck.towing_capacity())
