from entities.account import Account
from entities.branch import Branch


class SavingAccount(Account):
    def __init__(self, branch: Branch, number: str):
        super().__init__(branch, number)

    def withdraw(self, amount: float):
        if amount > self._balance:
            print("You don't have enough money to withdraw the amount required.")
            return
        self._balance -= amount
