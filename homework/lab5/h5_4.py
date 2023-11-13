from datetime import datetime

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def role(self):
        pass

    def __str__(self):
        return f"{self.name} ,  {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, employees=None, programs=None):
        super().__init__(name, salary)
        self.employees = employees if employees else []
        self.programs = programs

    def add_employee(self, employee):
        self.employees.append(employee)

    def count_employees(self):
        return len(self.employees)

    def role(self):
        return f"Manager ,  {self.name} ,  {self.salary} ,  Programs: {self.programs}"

class Engineer(Employee):
    def __init__(self, name, salary, language, time_in, time_out):
        super().__init__(name, salary)
        self.language = language
        self.time_in = time_in
        self.time_out = time_out

    def calculate_hours_worked(self):
        time_format = "%H:%M"
        in_time = datetime.strptime(self.time_in, time_format)
        out_time = datetime.strptime(self.time_out, time_format)
        delta = out_time - in_time
        return delta.total_seconds() / 3600

    def role(self):
        return f"Engineer ,  {self.name} ,  {self.salary} ,  {self.language} ,  {self.time_in} to {self.time_out}"

class Salesperson(Employee):
    def __init__(self, name, salary, products_sold):
        super().__init__(name, salary)
        self.products_sold = products_sold

    def calculate_revenue(self, product_prices):
        total_revenue = sum(product_prices.get(product, 0) * quantity for product, quantity in self.products_sold.items())
        return total_revenue

    def role(self):
        return f"Salesperson ,  {self.name} ,  {self.salary} ,  Products Sold: {self.products_sold}"


engineer = Engineer("Engineer", 2000, "Python", "09:00", "17:00")
print(engineer.role())
print(f"Hours worked: {engineer.calculate_hours_worked()} hours")

product_prices = {"Cars": 5000, "Laptops": 1000, "Phones": 800}
salesperson = Salesperson("Salesperson", 3000, {"Cars": 5, "Laptops": 10, "Phones": 20})
print(salesperson.role())
print(f"Revenue generated: ${salesperson.calculate_revenue(product_prices)}")


manager = Manager("Manager", 1000, employees=[], programs="Excel")
manager.add_employee(engineer)
manager.add_employee(salesperson)
print(manager.role())
print(f"Number of employees managed: {manager.count_employees()}")
