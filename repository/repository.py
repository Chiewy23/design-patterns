from abc import abstractmethod


class Contact:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        temp = ""
        if self is Friend:
            temp = f" Friend name: {self.name} Ph: {self.phone_number}"
        elif self is Work:
            temp = f" Work name: {self.name} Email: {self.email}"

        return temp


class Friend(Contact):
    def __init__(self, phone_number, name):
        super().__init__(name)
        self.phone_number = phone_number


class Work(Contact):
    def __init__(self, email, name):
        super().__init__(name)
        self.email = email


class RepositoryBase:
    @abstractmethod
    def append(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def get_all(self):
        pass


class InMemoryList(RepositoryBase):
    def __init__(self):
        self.list = []

    def append(self, item):
        self.list.append(item)

    def remove(self, item):
        self.list.remove(item)

    def get_all(self):
        result = ""

        for item in self.list:
            result += f"{item}\n"

        return result


class TextFileRepository(RepositoryBase):
    def __init__(self, file_name):
        self.file_name = file_name

    def append(self, item):
        print("Appending to text file.")

    def remove(self, item):
        print("Removing from text file.")

    def get_all(self):
        print("Printing all items in text file.")


class ContactUI:
    def __init__(self, repository):
        if repository is not RepositoryBase:
            raise Exception("Repository must be of type RepositoryBase")
        self.repository = repository

    def append(self, contact):
        self.repository.add(contact)

    def remove(self, contact):
        self.repository.remove(contact)

    def get_all_contacts(self):
        print(self.repository.get_all())
