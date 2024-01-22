from entities.account import Account
from entities.branch import Branch


class CheckingAccount(Account):
    def __init__(self, branch: Branch, number: str):
        super().__init__(branch, number)

    def withdraw(self, amount):
        if amount > (self._balance + self.__tax_management()):
            print("You don't have enough money to withdraw the amount required.")
            return
        self._balance -= self.__tax_management()
        self._balance -= amount

    def __tax_management(self):
        if self._balance < 10000:
            return self._balance * 0.003
        else:
            return 30 + (self._balance - 10000) * 0.0045
