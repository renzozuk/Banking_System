from entities.account import Account
from entities.branch import Branch


class CheckingAccount(Account):
    def __init__(self, branch: Branch, number: str):
        super().__init__(branch, number)

    def withdraw(self, amount):
        self._balance -= amount
        self._balance -= self.__tax_management()

    def __tax_management(self):
        if self._balance < 10000:
            return self._balance * 0.05
        else:
            return 500 + (self._balance - 10000) * 0.075
