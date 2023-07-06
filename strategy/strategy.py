from abc import abstractmethod


class StrategyBase:
    @abstractmethod
    def execute(self, int1, int2):
        pass


class Add(StrategyBase):
    def execute(self, int1, int2):
        return int1 + int2


class Multiply(StrategyBase):
    def execute(self, int1, int2):
        return int1 * int2


class Subtract(StrategyBase):
    def execute(self, int1, int2):
        return int1 - int2


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, int1, int2):
        return self.strategy.execute(int1, int2)


if __name__ == "__main__":
    pass
