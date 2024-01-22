from entities.branch import Branch
from entities.customer import Customer
from entities.account import Account
from entities.checking_account import CheckingAccount
from entities.saving_account import SavingAccount
from util.generator import generate_account_number


class Bank:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__accounts = []
        self.__branches = []
        self.__customers = []
        self.__current_customer = None
        self.__current_account = None
        self.__branches.append(Branch("0001"))

    @property
    def current_customer(self) -> Customer:
        return self.__current_customer

    @property
    def current_account(self) -> Account:
        return self.__current_account

    def __add_account(self, branch: Branch, customer: Customer, account: Account) -> bool:
        if branch not in self.__branches:
            print("This branch doesn't belong to this bank.")
            return False

        if customer not in self.__customers:
            print("This person is not customer of this bank.")
            return False

        self.__accounts.append(account)
        self.__current_customer.add_account(account)
        print(f"The account [Branch: {account.branch}] [Number account: {account.number}] was created successfully.")
        return True

    def add_saving_account(self, customer: Customer):
        self.__add_account(self.__branches[-1], customer, SavingAccount(self.__branches[-1], generate_account_number(customer)))

    def add_checking_account(self, customer: Customer):
        if customer.age < 18:
            print("A person must be 18 years old or older to open a checking account.")
            return

        self.__add_account(self.__branches[-1], customer, CheckingAccount(self.__branches[-1], generate_account_number(customer)))

    def add_branch(self):
         branch = Branch(str(len(self.__branches) + 1))
         self.__branches.append(branch)

    def add_customer(self, name, age, cpf, password) -> bool:
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False

        new_customer = Customer(name, age, cpf, len(self.__customers) + 1, password)

        for customer in self.__customers:
            if customer == new_customer:
                print("This person is already registered as a customer at this bank.")
                return False

        self.__customers.append(new_customer)

        print(f"Account created successfully, your login is {new_customer.login}")

        return True

    def customer_login(self, login, password) -> bool:
        for customer in self.__customers:
            if customer.login == login and customer.password == password:
                self.__current_customer = customer
                print("Logged in successfully.")
                return True

        print("Login or password incorrect.")
        return False

    def customer_logout(self):
        self.__current_account = None
        self.__current_customer = None

    def account_login(self):
        if self.__current_customer is None:
            return False

        self.__current_account = self.current_customer.login_account()

    def account_logout(self):
        self.__current_account = None
