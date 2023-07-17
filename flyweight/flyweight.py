class FontProperty:
    def __init__(self, letter, font_size=12, colour="black"):
        self.letter = letter
        self.font_size = font_size
        self.colour = colour

    def display(self):
        print(self.letter)


class Memory:
    def __init__(self):
        self.items = {}

    def lookup(self, letter):
        if letter not in self.items:
            self.items[letter] = FontProperty(letter)

        return self.items[letter]

    def total_objects_made(self):
        return len(self.items)


class Document:
    def __init__(self):
        self.memory = Memory()
        self.letters = []

    def type_letter(self, letter):
        font_prop = self.memory.lookup(letter)
        self.letters.append(font_prop)

    def process(self):
        for letter in self.letters:
            print(letter)
