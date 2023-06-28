from singleton.singleton import Singleton


# ----- SINGLETON PATTERN -----
singleton1 = Singleton(name="Bob")
singleton2 = Singleton()

print(singleton1 is singleton2)
print(singleton1.name)


if __name__ == '__main__':
    pass

