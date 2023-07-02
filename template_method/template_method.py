class ExcelFile:
    def read_data(self):
        print(f"Reads data from excel file - {self}")

    def process_data(self):
        print(f"Processes data from excel file - {self}")

    def save_data(self):
        print(f"Saves data to Db - {self}")


class TextFile:
    def read_data(self):
        print(f"Reads data from text file - {self}")

    def process_data(self):
        print(f"Processes data from text file - {self}")

    def save_data(self):
        print(f"Saves data to Db - {self}")


if __name__ == "__main__":
    pass
