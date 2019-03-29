class C:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return "<{} and {}>".format(self.num1, self.num2)

    def __repr__(self):
        return "[{}, {}]".format(self.num1, self.num2)

    def __eq__(self, other):
        if self.__repr__() == other.__repr__():
            return True

    def __add__(self, other):
        num1 = self.num1 + other.num1
        try:
            num2 = self.num2 + other.num2
        except TypeError:
            return self.__class__(num1, self.num1 + other.num2)
        return self.__class__(num1, num2)

    def reverse(self):
        num = self.num1
        self.num1 = self.num2
        self.num2 = num

    def reversed(self):
        return self.__class__(self.num2, self.num1)


class D(C):
    def __init__(self, num1, num2=None):
        super().__init__(num1, num2)

    def __str__(self):
        return "<Just {}>".format(self.num1)

    def __eq__(self, other):
        if self.num1 == other.num1 or self.num2 == self.num2:
            return True


class Door:
    bool_1 = [("Closed", True), ("Open", False)]
    bool_2 = [("unlocked", False), ("locked", True)]

    def __init__(self, bool1, bool2):
        self.bool1 = bool1
        self.bool2 = bool2

    @property
    def closed(self):
        return self.bool1

    @property
    def locked(self):
        return self.bool2

    def __str__(self):
        return "{} and {} door".format(([i[0] for i in Door.bool_1 if self.bool1 == i[1]][0]),
                                       ([j[0] for j in Door.bool_2 if self.bool2 == j[1]][0]))

    def turnKey(self):
        self.bool2 = not self.bool2

    def __eq__(self, other):
        if isinstance(self, Door) and isinstance(other, Door):
            if [self.bool1, self.bool2] == [other.bool1, other.bool2]:
                return True
        return False

    def __hash__(self):
        return hash((self.bool1, self.bool2))