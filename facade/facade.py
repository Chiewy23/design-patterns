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


if __name__ == "__main__":
    pass
