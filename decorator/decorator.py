from abc import abstractmethod


class IceCreamBase:
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    def print_details(self):
        print(f"Cost: £{self.cost()}, Description: {self.get_description()}")


class ChocolateIceCream(IceCreamBase):
    def get_description(self):
        return "Chocolate ice cream"

    def cost(self):
        return 2.00


class VanillaIceCream(IceCreamBase):
    def get_description(self):
        return "Vanilla ice cream"

    def cost(self):
        return 1.00


class IceCreamDecorator(IceCreamBase):
    seperator = ", "

    def __init__(self, topping=IceCreamBase()):
        self.topping = topping

    def get_description(self):
        return self.topping.get_description()

    def cost(self):
        return self.topping.cost()
