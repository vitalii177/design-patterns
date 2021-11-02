import copy


class Customer:
    def __init__(self, customer_id: int, name: str, address: str, phone_number: str, acct_number: int, bank):
        self.id = customer_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.acct_number = acct_number
        self.bank = bank

        self.accounts = []
        self.loans = []

    def generalInquiry(self):
        pass

    def depositMemory(self):
        pass

    def withdrawMoney(self):
        pass

    def openAccount(self, teller, account_id: int):
        teller.openAccount(self, account_id)

    def closeAccount(self, teller, account_id: int):
        teller.closeAccount(self, account_id)

    def applyForLoan(self, teller, loan_id: int, loan_type: str, account_id: int):
        teller.loanRequest(self, loan_id, loan_type, account_id)

    def requestCard(self):
        pass

    def __copy__(self):
        customer = self.__class__(self.id, self.name, self.address, self.phone_number,
                                  self.acct_number, self.bank)
        customer.__dict__.update(self.__dict__)
        return customer

    def __deepcopy__(self, memo):
        customer = self.__class__(self.id, self.name, self.address, self.phone_number,
                                  self.acct_number, self.bank)
        customer.__dict__ = copy.deepcopy(self.__dict__, memo)
        return customer

    def __str__(self):
        return f"Customer[Bank[id={self.bank.id},name={self.bank.name}, location={self.bank.location}]," \
               f"id={self.id},name={self.name},address={self.address},phone_number={self.phone_number}," \
               f"acct_number={self.acct_number}]"


class Teller:
    def __init__(self, teller_id: int, name: str, bank):
        self.id = teller_id
        self.name = name
        self.bank = bank

    def collectMoney(self):
        pass

    def openAccount(self, customer: Customer, account_id: int):
        if account_id not in customer.accounts:
            customer.accounts[account_id] = Account(account_id, customer.id)
            print(f"An account with id={account_id} has opened successfully!")

    def closeAccount(self, customer: Customer, account_id: int):
        if account_id in customer.accounts:
            print(f"An account with id={account_id} has closed successfully!")
            del customer.accounts[account_id]

    def loanRequest(self, customer: Customer, loan_id: int, loan_type: str, account_id: int):
        self.openAccount(customer, account_id)
        if loan_id not in customer.loans:
            customer.loans[loan_id] = Loan(loan_id, loan_type, account_id, customer.id)

    def provideInfo(self):
        pass

    def issueCard(self):
        pass


class Bank:
    def __init__(self, bank_id: int, name: str, location: str):
        self.id = bank_id
        self.name = name
        self.location = location
        self.tellers = []
        self.customers = []


class Account:
    def __init__(self, account_id: int, customer_id: int):
        self.id = account_id
        self.customer_id = customer_id


class Loan:
    def __init__(self, loan_id: int, type: str, account_id: int, customer_id: int):
        self.id = loan_id
        self.type = type
        self.account_id = account_id
        self.customer_id = customer_id


class Checking(Account):
    pass


class Savings(Account):
    pass


# The client
bank = Bank(1, 'HSBC Bank Plc', 'England')
customer = Customer(customer_id=1, name='Julia', address='3455 Br. Street',
                    phone_number='324-x34-23-664', acct_number=1, bank=bank)
customer_copy = customer.__copy__()
customer_deep_copy = customer.__deepcopy__({})
print(f"Customer: {customer.__str__()}")
print(f"Customer(copy): {customer_copy.__str__()}")
print(f"Customer(deepcopy): {customer_deep_copy.__str__()}")






