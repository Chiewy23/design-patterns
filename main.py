from singleton.singleton import Singleton
from factory.factory import CalculatorFactory
from template_method.template_method import ExcelFile, TextFile
from adapter.adapter import Adapter
from facade.facade import InsuranceFacade
from strategy.strategy import Context, Add, Subtract, Multiply
from state.state import StateContext, StateOnline
from proxy.proxy import ProxyServer


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


# ----- FACADE -----
def facade_example():
    insurance_facade = InsuranceFacade(vin=34, dob="21.08.1996", state="Texas")
    insurance_facade.get_quote()


# ----- STRATEGY -----
def strategy_example():
    strategy_add = Context(Add())
    strategy_subtract = Context(Subtract())
    strategy_multiply = Context(Multiply())

    print(strategy_add.execute_strategy(1, 2))
    print(strategy_subtract.execute_strategy(1, 2))
    print(strategy_multiply.execute_strategy(1, 2))


# ----- STATE -----
def state_example():
    state_context = StateContext()
    print(f"Is meeting online: {state_context.is_meeting_online()}")

    state_context.set_current_state(StateOnline())
    print(f"Is meeting online: {state_context.is_meeting_online()}")


# ----- STATE -----
def proxy_example():
    tweet1 = ProxyServer("@BillGates", "Pass123")
    tweet2 = ProxyServer("@BillGates", "Pass1234")

    tweet1.display_tweets()
    tweet2.display_tweets()


if __name__ == '__main__':
    # singleton_example()
    # factory_example()
    # template_method_example()
    # adapter_example()
    # facade_example()
    # strategy_example()
    # state_example()
    proxy_example()

