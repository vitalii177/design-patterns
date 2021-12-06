from abc import ABCMeta, abstractmethod


class IAcct(metaclass=ABCMeta):
    @abstractmethod
    def get_balance(self) -> int:
        pass

    @abstractmethod
    def withdraw(self, amount: int) -> bool:
        pass

    @abstractmethod
    def attach_customer(self, customer) -> None:
        pass

    @abstractmethod
    def detach_customer(self, customer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class IDB(metaclass=ABCMeta):
    @abstractmethod
    def login(self, account_id: str) -> IAcct:
        pass

    @abstractmethod
    def logout(self, a: IAcct):
        pass


class AccountProxy(IAcct):
    def __init__(self, balance: int):
        self._balance = balance
        self._customers = []
        self.account = Account(self)

    def get_balance(self) -> int:
        self.notify()
        return self.account.get_balance()

    def deposit(self, amount: int) -> bool:
        return self.account.deposit(amount)

    def withdraw(self, amount: int) -> bool:
        return self.account.withdraw(amount)

    def attach_customer(self, customer) -> None:
        self.account.attach_customer(customer)
        self._customers.append(customer)

    def detach_customer(self, customer) -> None:
        self.account.detach_customer(customer)
        self._customers.remove(customer)

    def notify(self) -> None:
        self.account.notify()
        for customer in self._customers:
            customer.notify(self)


class Account(IAcct):
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0

    def get_balance(self) -> int:
        return self.balance

    def deposit(self, amount: int) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: int) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def attach_customer(self, customer) -> None:
        print(f"IAcct: Attached a customer with id={customer.id}.")
    
    def detach_customer(self, customer) -> None:
        print(f"IAcct: Detached a customer with id={customer.id}.")

    def notify(self) -> None:
        print("IAcct: Notifying customers...")


class AccountDatabase(IDB):
    def login(self, account_id: str):
        print("You have logged in successfully!")
        return Account(account_id)

    def logout(self, a: IAcct):
        print("You have logged out successfully!")


class DatabaseProxy(IDB):
    def __init__(self, real_database: AccountDatabase):
        self.real_database = real_database
        self.real_account = None

    def login(self, account_id: str) -> IAcct:
        self.real_account = self.real_database.login(account_id)
        balance = self.real_account.get_balance()
        return self.make_account_proxy(balance)

    def logout(self, a: IAcct):
        self.real_account.balance = a.get_balance()
        self.real_database.logout(self.real_account)

    def make_account_proxy(self, start_amount: int):
        return AccountProxy(start_amount)


class ATM:
    def __init__(self, database_proxy: DatabaseProxy):
        self.dbp = database_proxy

    def handle_balance_request(self) -> int:
        return self.dbp.real_account.get_balance()

    def handle_login(self, account_id: str) -> IAcct:
        return self.dbp.login(account_id)

    def handle_logout(self):
        return self.dbp.logout(self.dbp.real_account)

    def handle_deposit(self, amount: int) -> bool:
        return self.dbp.real_account.deposit(amount)

    def handle_withdrawal(self, amount: int, customer):
        return customer.withdraw(amount, self.dbp)


class Customer:
    def __init__(self, id: int, name: str, account_number: str):
        self.id = id
        self.name = name
        self.account_number = account_number

    def notify(self, account_proxy: AccountProxy):
        account_proxy.notify()
        print(f"Customer[id={self.id}, name={self.name}, account_number={self.account_number}]")

    def withdraw(self, amount: int, dbp: DatabaseProxy):
        return dbp.real_account.withdraw(amount)


# The client code
db = AccountDatabase()
dbp = DatabaseProxy(db)
atm = ATM(dbp)
customer = Customer(id=1, name='Mike', account_number='141-3425-353')
login = str(input("Do you want to log in [y/n]: "))
if login == 'y':
    an = str(input('Enter your account number: '))
    if an == customer.account_number:
        atm.handle_login(account_id='1')
        dbp.real_account.attach_customer(customer=customer)
        print("--OPTIONS--")
        print("1 - check balance")
        print("2 - deposit money")
        print("3 - withdraw money")
        print("4 - log out")
        choice = 0
        while choice != 4:
            choice = int(input('> '))
            if choice == 1:
                print(f"BALANCE: {atm.handle_balance_request()}$")
            elif choice == 2:
                amount = int(input('Enter amount of money to deposit: '))
                print(f"+{amount}$\n{atm.handle_deposit(amount)}")
            elif choice == 3:
                amount = int(input('Enter amount of money to withdrawal: '))
                print(f"-{amount}$\n{atm.handle_withdrawal(amount, customer)}")
        dbp.real_account.detach_customer(customer)
        atm.handle_logout()
elif login == 'n':
    print("OK")
