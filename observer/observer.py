from abc import abstractmethod


class SubjectBase:
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class ObserverBase:
    @abstractmethod
    def update(self, blog_article):
        pass

    @abstractmethod
    def print_article(self):
        pass


class Blog(SubjectBase):

    def __init__(self):
        self.observers_list = []
        self.state_change = False
        self.blog_article = ""

    def register_observer(self, observer):
        self.observers_list.append(observer)

    def remove_observer(self, observer):
        self.observers_list.remove(observer)

    def notify_observers(self):
        if self.state_change:
            for ob in self.observers_list:
                ob.update(self.blog_article)

            self.state_change = False

    def post_new_article(self, article):
        self.blog_article = article
        self.state_change = True
        self.notify_observers()


class User(ObserverBase):
    def __init__(self, blog=Blog()):
        self.blog = blog
        self.article = ""

        self.blog.register_observer(self)

    def update(self, blog_article):
        self.article = blog_article
        print(f"State change reported by subject - {self}.")

    def print_article(self):
        print(f"User {self} article: {self.article}")
