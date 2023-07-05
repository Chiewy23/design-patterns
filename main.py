from singleton.singleton import Singleton
from factory.factory import CalculatorFactory
from template_method.template_method import ExcelFile, TextFile
from adapter.adapter import Adapter
from facade.facade import InsuranceFacade


# ----- SINGLETON PATTERN -----
def singleton_example():
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)


# ----- FACTORY PATTERN -----
def factory_example():
    multiplier = CalculatorFactory.get_calculator("multiply")
    divider = CalculatorFactory.get_calculator("divide")

    print(type(multiplier))
    print(type(divider))

    print(multiplier.calculate(2, 4))
    print(divider.calculate(4, 2))


# ----- TEMPLATE METHOD -----
def template_method_example():
    text_file_processor = TextFile()
    excel_processor = ExcelFile()

    text_file_processor.execute()
    print("\n")
    excel_processor.execute()


# ----- ADAPTER -----
def adapter_example():
    adapter = Adapter()
    result = adapter.connect_to_file_system(12345)
    print(result)


# ----- ADAPTER -----
def facade_example():
    insurance_facade = InsuranceFacade(vin=34, dob="21.08.1996", state="Texas")
    insurance_facade.get_quote()


if __name__ == '__main__':
    # singleton_example()
    # factory_example()
    # template_method_example()
    # adapter_example()
    facade_example()

