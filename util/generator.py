from entities.customer import Customer


def generate_account_number(customer: Customer) -> str:
    digit = (int(customer.cpf[6]) + int(customer.cpf[7]) + int(customer.id[-1])) % 10
    return f"{customer.cpf[6:9]}{customer.id}-{digit}"
