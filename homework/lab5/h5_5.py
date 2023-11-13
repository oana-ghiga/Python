#Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, Bird, and Fish. Add properties and methods to represent characteristics unique to each animal group.
#Mammals will have fur or hair, give birth to live young, and produce milk, calculate how much milk they produce in a year and how much they eat in a year.
#Birds will have feathers, lay eggs, and fly, calculate how many eggs they lay in a year and how much they fly in a day given their speed and rest times.
#Fish will have gills, live in water, and swim, calculate how much they swim in a day given their speed and rest times and the average number of gills the fish in our group have.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def sleep(self):
        pass

    def __str__(self):
        return f"{self.name}"

class Mammal(Animal):
    def __init__(self, name, fur, birth, milk_production, food_per_day):
        super().__init__(name)
        self.fur = fur
        self.birth = birth
        self.milk_production = milk_production
        self.food_per_day = food_per_day

    def calculate_yearly_milk_production(self):
        return self.milk_production * 365

    def calculate_yearly_food_consumption(self):
        return self.food_per_day * 365

    def sleep(self):
        return 8

    def __str__(self):
        return f"{self.name} - {self.fur} - {self.birth} - Milk Production: {self.milk_production} liters - Food per day: {self.food_per_day}"

class Bird(Animal):
    def __init__(self, name, feathers, eggs_production, fly_speed, rest_hours_per_day, food_per_day):
        super().__init__(name)
        self.feathers = feathers
        self.eggs_production = eggs_production
        self.fly_speed = fly_speed
        self.rest_hours_per_day = rest_hours_per_day
        self.food_per_day = food_per_day

    def calculate_yearly_eggs_production(self):
        return self.eggs_production * 365

    def calculate_daily_flight_distance(self):
        active_hours_per_day = 24 - self.rest_hours_per_day
        return self.fly_speed * active_hours_per_day

    def eat(self):
        return self.food_per_day

    def sleep(self):
        return self.rest_hours_per_day

    def __str__(self):
        return f"{self.name} , {self.feathers} , Eggs Production: {self.eggs_production} eggs , Fly Speed: {self.fly_speed} km/h , Rest Hours per Day: {self.rest_hours_per_day} hours , Food per day: {self.food_per_day}"

class Fish(Animal):
    def __init__(self, name, gills, swim_speed, rest_hours_per_day, gills_production, food_per_day):
        super().__init__(name)
        self.gills = gills
        self.swim_speed = swim_speed
        self.rest_hours_per_day = rest_hours_per_day
        self.gills_production = gills_production
        self.food_per_day = food_per_day

    def calculate_daily_swimming_distance(self):
        active_hours_per_day = 24 - self.rest_hours_per_day
        return self.swim_speed * active_hours_per_day

    def eat(self):
        return self.food_per_day

    def __str__(self):
        return f"{self.name} , {self.gills} , Swim Speed: {self.swim_speed} km/h , Rest Hours per Day: {self.rest_hours_per_day} hours , Gills: {self.gills_production} , Food per day: {self.food_per_day}"


mammal = Mammal("Mammal", "fur", "live birth", 100, 5)
print(mammal)
print("Yearly Milk Production:", mammal.calculate_yearly_milk_production(), "liters")
print("Yearly Food Consumption:", mammal.calculate_yearly_food_consumption(), "kilograms")
print("Sleep:", mammal.sleep(), "hours")

bird = Bird("Bird", "feathers", 50, 30, 6, 3)
print(bird)
print("Yearly Eggs Production:", bird.calculate_yearly_eggs_production(), "eggs")
print("Daily Flight Distance:", bird.calculate_daily_flight_distance(), "km")
print("Eat:", bird.eat(), "grams")
print("Sleep:", bird.sleep(), "hours")

fish1 = Fish("Fish1", "gills", 20, 10, 80, 2)
fish2 = Fish("Fish2", "gills", 25, 8, 90, 3)
fish3 = Fish("Fish3", "gills", 18, 12, 70, 1)

fish_group = [fish1, fish2, fish3]

# Calculate the average gills production for the fish group
average_gills_production = sum(fish.gills_production for fish in fish_group) / len(fish_group)

for fish in fish_group:
    print(fish)

print("Average Gills Production for the Fish Group:", average_gills_production)
print("Eat:", fish1.eat(), "grams")
print("Sleep:", fish1.sleep(), "hours")
print("Daily Swimming Distance:", fish1.calculate_daily_swimming_distance(), "km")
