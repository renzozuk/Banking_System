import re
from entities.account import Account
from entities.person import Person


class Customer(Person):
    def __init__(self, name, age, cpf, id: int, password):
        super().__init__(name, age, cpf)
        self.__id = f"{id}"
        self.__accounts = []

        name_match = re.findall(r'\b(\w+)\b', name)

        if name_match and name_match[0] != name_match[-1]:
            self.__login = '.'.join([name_match[0], name_match[-1]]) + "." + self.__id
        else:
            self.__login = name + "." + self.__id

        self._password = password

    @property
    def id(self):
        return self.__id

    @property
    def login(self) -> str:
        return self.__login

    @property
    def password(self) -> str:
        return self._password

    def add_account(self, account: Account):
        self.__accounts.append(account)

    def remove_account(self, account: Account):
        self.__accounts.remove(account)

    def login_account(self, branch_number, number):
        for account in self.__accounts:
            if account.branch.number == branch_number and account.number == number:
                return account
        return None

    @property
    def total_amount(self) -> str:
        total = 0.0

        for account in self.__accounts:
            total += account.get_balance

        return f"Your total amount: ${total:.2f}"

    def __eq__(self, other):
        super.__eq__(self, other)
