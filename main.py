from singleton.singleton import Singleton


# ----- SINGLETON PATTERN -----
def singleton_example():
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)


def factory_example():
    pass


if __name__ == '__main__':
    singleton_example()

