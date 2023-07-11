from abc import abstractmethod


class ChainBase:
    @abstractmethod
    def calculate(self, request):
        pass

    @abstractmethod
    def set_next_chain(self, next_chain):
        pass


class Numbers:
    def __init__(self, new_num1, new_num2, calc_wanted):
        self.new_num1 = new_num1
        self.new_num2 = new_num2
        self.calc_wanted = calc_wanted


class AddNumbers(ChainBase):
    next_in_chain = None

    def calculate(self, request):
        if request.calc_wanted == "add":
            return request.new_num1 + request.new_num2
        else:
            return self.next_in_chain.calculate(request)

    def set_next_chain(self, next_chain):
        self.next_in_chain = next_chain


class SubtractNumbers(ChainBase):
    next_in_chain = None

    def calculate(self, request):
        if request.calc_wanted == "subtract":
            return request.new_num1 - request.new_num2
        else:
            return self.next_in_chain.calculate(request)

    def set_next_chain(self, next_chain):
        self.next_in_chain = next_chain


class MultiplyNumbers(ChainBase):
    next_in_chain = None

    def calculate(self, request):
        if request.calc_wanted == "multiply":
            return request.new_num1 * request.new_num2
        else:
            return self.next_in_chain.calculate(request)

    def set_next_chain(self, next_chain):
        self.next_in_chain = next_chain

