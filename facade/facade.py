class Car:
    def __init__(self, vin):
        self.vin = vin

    def check_car_history(self):
        print(f"Check car history: {self.vin}")

    def check_car_safety(self):
        print(f"Check car safety: {self.vin}")


class Driver:
    def __init__(self, dob):
        self.dob = dob

    def check_driver_details(self):
        print(f"Check driver history: {self.dob}")


class Location:
    def __init__(self, state):
        self.state = state

    def check_driving_conditions(self):
        print(f"Get location information for {self.state}")


class InsuranceFacade:
    def __init__(self, vin=1, dob="01.01.2001", state="Unassigned"):
        self.car = Car(vin)
        self.driver = Driver(dob)
        self.location = Location(state)

    def get_quote(self):
        # Invoke the methods in the order required.
        self.car.check_car_safety()
        self.car.check_car_history()

        self.driver.check_driver_details()

        self.location.check_driving_conditions()


if __name__ == "__main__":
    pass
