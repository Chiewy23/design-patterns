from abc import abstractmethod


class InsuranceBuilderBase:
    @abstractmethod
    def build_driver(self):
        pass

    @abstractmethod
    def build_vehicle(self):
        pass

    @abstractmethod
    def build_location(self):
        pass

    @abstractmethod
    def get_insurance(self):
        pass


class Driver:
    def __init__(self, name="No Name", age=99):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


class Location:
    def __init__(self, zip_code="No Zipcode"):
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.zip_code}"


class Vehicle:
    def __init__(self, model="No model", year=9999):
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.model} ({self.year})"


class Insurance:
    def __init__(self, driver=Driver(), location=Location(), vehicle=Vehicle(), price=0.00):
        self.driver = driver
        self.location = location
        self.vehicle = vehicle
        self.price = price

    def __str__(self):
        return f"Insurance has these values: \n {self.driver} \n {self.location} \n {self.vehicle} \n {self.price}"


class AutoBuilder(InsuranceBuilderBase):
    def __init__(self):
        self.insurance = Insurance()

    def build_driver(self):
        pass

    def build_vehicle(self):
        pass

    def build_location(self):
        pass

    def get_insurance(self):
        pass


class BoatBuilder(InsuranceBuilderBase):
    def build_driver(self):
        pass

    def build_vehicle(self):
        pass

    def build_location(self):
        pass

    def get_insurance(self):
        pass
