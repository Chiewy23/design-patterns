from abc import abstractmethod


class Calculate:
    @abstractmethod
    def calculate(self, *args, **kwargs):
        pass


class Divide(Calculate):
    def calculate(self, a, b):
        try:
            return float(a / b)
        except ValueError as err:
            print("Please provide float arguments")
            return 0


class Multiply(Calculate):
    def calculate(self, a, b):
        try:
            return float(a * b)
        except ValueError as err:
            print("Please provide float or integer arguments")
            return 0


class CalculatorFactory:
    @staticmethod
    def get_calculator(calculator_type):
        if calculator_type.lower() == "divide":
            return Divide()

        if calculator_type.lower() == "multiply":
            return Multiply()

        return None
