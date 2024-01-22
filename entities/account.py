from abc import ABC, abstractmethod
from entities.branch import Branch


class Account(ABC):
    def __init__(self, branch: Branch, number: str):
        self.__balance = 0.0
        self.__branch = branch
        self.__number = number

    @property
    def _balance(self):
        return self.__balance

    def get_balance(self):
        return self.__balance

    @_balance.setter
    def _balance(self, value):
        assert isinstance(value, float)
        self.__balance = value

    @property
    def branch(self):
        return self.__branch

    @property
    def number(self):
        return self.__number

    def deposit(self, amount: float):
        self.__balance += amount

    @abstractmethod
    def withdraw(self, amount: float):
        ...

    def transfer(self, other, amount: float):
        self.withdraw(amount)
        other.deposit(amount)

    def __eq__(self, other):
        return self.__branch == other.__branch and self.__number == other.__number

    def __str__(self):
        return (f"==============================\n"
                f"Bank statement:\n"
                f"Branch: {self.__branch.number}\n"
                f"Number account: {self.__number}\n"
                f"Balance: ${self.__balance:.2f}\n"
                f"==============================")
