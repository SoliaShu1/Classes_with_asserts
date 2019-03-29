import copy


class A:
    """A representation class"""
    def __init__(self, *arg):
        """Initializing numbers list, evens, odds"""
        self.numbers = arg
        self.evens = sorted([i for i in arg if i % 2 == 0])
        self.odds = [i for i in arg if i % 2 != 0]

    def __str__(self):
        """Method for representing"""
        return "A(evens={},odds={})".format(self.evens, self.odds)

    def __eq__(self, other):
        """Method for checking equality"""
        if isinstance(self, A) and isinstance(other, A):
            return self.evens == other.evens
        return False

    def clearOdds(self):
        """Method that clears odds list"""
        self.odds = []

    def clearedOdds(self):
        """Method for cleared odds"""
        new = copy.copy(self)
        new.clearOdds()
        return new


class B(A):
    """B representing class"""
    def __init__(self, *arg):
        """Initializing numbers list, evens and odds"""
        super().__init__(*arg)
        self.numbers = [i for i in range(self.numbers[0], self.numbers[1] + 1)]
        self.evens = sorted([i for i in self.numbers if i % 2 == 0])
        self.odds = [i for i in self.numbers if i % 2 != 0]

    def shifted(self, num):
        """Method that adds a number to each coordinate"""
        new = copy.copy(self)
        new.numbers = [i + num for i in new.numbers]
        new.evens = sorted([i for i in new.numbers if i % 2 == 0])
        new.odds = [i for i in new.numbers if i % 2 != 0]
        return new

    def __str__(self):
        """Method for representing"""
        return "B(evens={},odds={})".format(self.evens, self.odds)


