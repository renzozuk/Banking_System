from entities.bank import Bank

########################################################################################################################

bank = Bank("Bank", "1")

bank.add_customer("Yato Yamaguchi", 16, "123.456.789-00", "yat_")
bank.add_customer("Yato Yamaguchi", 16, "123.456.789-00", "yama_yat2008")
bank.add_customer("John Smith de Oliveira", 45, "098.765.432-10", "abracadabra")
bank.add_customer("Mary", 37, "246.802.468-13", "123456789")

########################################################################################################################

bank.customer_login("Yato.Yamaguchi.1", "I forgot my password")
bank.customer_login("Yato.Yamaguchi.1", "yama_yat2008")

bank.add_checking_account(bank.current_customer)
bank.add_saving_account(bank.current_customer)

# The user has to log in as a user before enter its account, because the user can have more than 1 account

bank.account_login()

yato_account = bank.current_account

print(yato_account)

yato_account.deposit(311.15)
yato_account.withdraw(350)
yato_account.withdraw(150)

print(yato_account)

bank.customer_logout()

########################################################################################################################

bank.customer_login("John.Oliveira.2", "abracadabra")

bank.add_checking_account(bank.current_customer)

bank.account_login()

john_account = bank.current_account

print(john_account)

john_account.deposit(5000)
john_account.withdraw(4500)

print(john_account)

john_account.transfer(yato_account, 100)

print(john_account)

print(yato_account)

bank.customer_logout()

########################################################################################################################
