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
        driver_name = input("Enter driver name: ")
        driver_age = int(input("Enter driver age: "))
        self.insurance.driver = Driver(driver_name, driver_age)

    def build_vehicle(self):
        vehicle_model = input("Enter vehicle model: ")
        vehicle_year = int(input("Enter vehicle year: "))
        self.insurance.vehicle = Vehicle(vehicle_model, vehicle_year)

    def build_location(self):
        zipcode = input("Enter Zipcode: ")
        self.insurance.location = Location(zipcode)

    def get_insurance(self):
        print(self.insurance)


class BoatBuilder(InsuranceBuilderBase):
    def __init__(self):
        self.insurance = Insurance()

    def build_driver(self):
        driver_name = input("Enter Captain name: ")
        driver_age = int(input("Enter Captain age: "))
        self.insurance.driver = Driver(driver_name, driver_age)

    def build_vehicle(self):
        vehicle_model = input("Enter boat model: ")
        vehicle_year = int(input("Enter boat year: "))
        self.insurance.vehicle = Vehicle(vehicle_model, vehicle_year)

    def build_location(self):
        zipcode = input("Enter Ocean location: ")
        self.insurance.location = Location(zipcode)

    def get_insurance(self):
        print(self.insurance)


class EngineerDirector:
    def __init__(self, insurance_builder):
        self.insurance_builder = insurance_builder

    def return_insurance(self):
        return self.insurance_builder.get_insurance()

    def construct_insurance(self):
        # Here you can define the order in which components are created.
        self.insurance_builder.build_location()
        self.insurance_builder.build_vehicle()
        self.insurance_builder.build_driver()
