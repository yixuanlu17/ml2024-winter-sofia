
class NumberStorage:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1  # Returning index + 1 to match the 1 to N indexing
        else:
            return -1
