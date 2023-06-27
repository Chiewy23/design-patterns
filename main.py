from singleton.singleton import Singleton


# ----- SINGLETON PATTERN -----
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)

if __name__ == '__main__':
    pass

