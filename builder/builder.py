class Insurance:
    def __init__(self, driver, location, vehicle, price):
        self.driver = driver
        self.location = location
        self.vehicle = vehicle
        self.price = price

    def __str__(self):
        return f"Insurance has these values: \n {self.driver} \n {self.location} \n {self.vehicle} \n {self.price}"


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


class Location:
    def __init__(self, zip_code):
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.zip_code}"


class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.model} ({self.year})"


