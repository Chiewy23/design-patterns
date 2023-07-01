from abc import abstractmethod, ABC


class Calculate:
    @abstractmethod
    def calculate(self, *args, **kwargs):
        pass


class Divide(Calculate):
    def calculate(self, a, b):
        return a / b


class Multiply(Calculate):
    def calculate(self, a, b):
        return a * b


class CalculateFactory:
    @staticmethod
    def get_calculator(calculator_type):
        if calculator_type.lower() == "divide":
            return Divide()

        if calculator_type.lower() == "multiply":
            return Multiply()

        return None
