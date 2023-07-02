from abc import abstractmethod


class DataProcessor:
    def execute(self):
        self.__read_data__()
        self.__process_data__()
        self.__save_data__()

    @abstractmethod
    def __read_data__(self):
        pass

    @abstractmethod
    def __process_data__(self):
        pass

    def __save_data__(self):
        print(f"Saves data to Db - {self}")


class ExcelFile(DataProcessor):
    def __read_data__(self):
        print(f"Reads data from excel file - {self}")

    def __process_data__(self):
        print(f"Processes data from excel file - {self}")


class TextFile(DataProcessor):
    def __read_data__(self):
        print(f"Reads data from text file - {self}")

    def __process_data__(self):
        print(f"Processes data from text file - {self}")


if __name__ == "__main__":
    pass
