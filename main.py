from singleton.singleton import Singleton


# ----- SINGLETON PATTERN -----
singleton1 = Singleton(name="Bob")
print(singleton1.name)
print(Singleton.name)

singleton2 = Singleton(name="Trevor")
print(singleton1.name)
print(Singleton.name)

print(singleton1 is singleton2)


if __name__ == '__main__':
    pass

