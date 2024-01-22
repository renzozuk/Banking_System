class Branch:
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return self.__number

    def __eq__(self, other):
        return self.number == other.number

    def __str__(self):
        return str(self.__number)
