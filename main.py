from singleton.singleton import Singleton
from factory.factory import CalculateFactory


# ----- SINGLETON PATTERN -----
def singleton_example():
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)


# ----- FACTORY PATTERN -----
def factory_example():
    multiplier = CalculateFactory.get_calculator("multiply")
    divider = CalculateFactory.get_calculator("divide")
    print(type(multiplier))
    print(type(divider))

    print(multiplier.calculate(2, 4))
    print(divider.calculate(4, 2))


if __name__ == '__main__':
    # singleton_example()
    factory_example()

