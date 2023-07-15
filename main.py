from bridge.bridge import SalesDepartment, FullTimeEmployee, ITDepartment, PartTimeEmployee
from builder.builder import AutoBuilder, EngineerDirector
from composite.composite import Developer, Manager
from decorator.decorator import ChocolateIceCream, NutsTopping, GummyTopping
from observer.observer import Blog, User
from singleton.singleton import Singleton
from factory.factory import CalculatorFactory
from template_method.template_method import ExcelFile, TextFile
from adapter.adapter import Adapter
from facade.facade import InsuranceFacade
from strategy.strategy import Context, Add, Subtract, Multiply
from state.state import StateContext, StateOnline
from proxy.proxy import ProxyServer
from chain_of_responsibility.chain_of_responsibility import Numbers, MultiplyNumbers, AddNumbers, SubtractNumbers


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


# ----- PROXY -----
def proxy_example():
    tweet1 = ProxyServer("@BillGates", "Pass123")
    tweet2 = ProxyServer("@BillGates", "Pass1234")

    tweet1.display_tweets()
    tweet2.display_tweets()


# ----- CHAIN OF RESPONSIBILITY -----
def chain_of_responsibility_example():
    request = Numbers(5, 5, "multiply")
    obj1 = AddNumbers()
    obj2 = SubtractNumbers()
    obj3 = MultiplyNumbers()

    obj1.set_next_chain(obj2)
    obj2.set_next_chain(obj3)
    obj3.set_next_chain(obj1)

    print(f"Result: {obj1.calculate(request)}")


# ----- BRIDGE -----
def bridge_example():
    dep1 = SalesDepartment(FullTimeEmployee())
    dep2 = ITDepartment(PartTimeEmployee())

    dep1.assign_employee()
    dep2.assign_employee()


# ----- COMPOSITE -----
def composite_example():
    dev1 = Developer(name="Charlie", salary=120000)
    dev2 = Developer(name="Hannah", salary=120000)

    manager1 = Manager(name="Jordan", salary=220000)
    manager1.add_employee(dev1)
    manager1.add_employee(dev2)

    director1 = Manager(name="Suzanne", salary=320000)
    director1.add_employee(manager1)

    director1.print()
    print("--------------------------------------------")
    manager1.print()


# ----- DECORATOR -----
def decorator_example():
    chocolate_ice_cream = ChocolateIceCream()

    chocolate_ice_cream = NutsTopping(chocolate_ice_cream)
    chocolate_ice_cream = GummyTopping(chocolate_ice_cream)

    chocolate_ice_cream.print_details()


# ----- OBSERVER -----
def observer_example():
    blog = Blog()
    user1 = User(blog)
    user2 = User(blog)

    blog.post_new_article("This is the newest article")
    user1.print_article()
    user2.print_article()


# ----- BUILDER -----
def builder_example():
    mercedes_benz = AutoBuilder()
    engineer = EngineerDirector(mercedes_benz)

    engineer.construct_insurance()
    engineer.return_insurance()


if __name__ == '__main__':
    # singleton_example()
    # factory_example()
    # template_method_example()
    # adapter_example()
    # facade_example()
    # strategy_example()
    # state_example()
    # proxy_example()
    # chain_of_responsibility_example()
    # bridge_example()
    # composite_example()
    # decorator_example()
    # observer_example()
    builder_example()
