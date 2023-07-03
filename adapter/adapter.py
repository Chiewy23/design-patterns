from abc import abstractmethod


class ClientBase:
    @abstractmethod
    def connect_to_file_system(self, customer_id):
        pass


class VendorBase:
    @abstractmethod
    def connect_to_db(self, connection_string, customer_id):
        pass

    @abstractmethod
    def get_age(self):
        pass


class ClientSystem(ClientBase):
    def connect_to_file_system(self, customer_id):
        print(f"Connects to file system and fetches client age: {customer_id}")
        return 65


class VendorSystem(VendorBase):
    def __init__(self):
        self.age = None

    def connect_to_db(self, connection_string, customer_id):
        print(f"Connects to db and fetches customer age: {connection_string} & {customer_id}")
        self.age = 55

    def get_age(self):
        return self.age


class Adapter(ClientBase):

    def __init__(self, vendor=VendorSystem()):
        self.vendor = vendor

    def connect_to_file_system(self, customer_id):
        connection_string = "Some connection string"
        self.vendor.connect_to_db(connection_string, customer_id)
        return self.vendor.get_age()


