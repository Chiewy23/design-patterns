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
