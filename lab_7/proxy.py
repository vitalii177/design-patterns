from abc import ABCMeta, abstractmethod


class IAcct(metaclass=ABCMeta):
    @abstractmethod
    def get_balance(self) -> int:
        pass

    @abstractmethod
    def withdraw(self, amount: int) -> bool:
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

    def get_balance(self) -> int:
        return self._balance

    def withdraw(self, amount: int) -> bool:
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False


class Account(IAcct):
    def __init__(self, account_id):
        self.account_id = account_id
        self.__balance = 2000

    def get_balance(self) -> int:
        return self.__balance

    def withdraw(self, amount: int) -> bool:
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False


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
        self.dbt = database_proxy

    def handle_balance_request(self) -> int:
        return self.dbt.real_account.get_balance()

    def handle_login(self, account_id: str) -> IAcct:
        return self.dbt.login(account_id)

    def handle_logout(self):
        return self.dbt.logout(self.dbt.real_account)

    def handle_withdrawal(self, amount: int):
        return self.dbt.real_account.withdraw(amount)


# The client code
db = AccountDatabase()
dbp = DatabaseProxy(db)
atm = ATM(dbp)
login = str(input("Do you want to log in [y/n]: "))
if login == 'y':
    atm.handle_login(account_id='1')
    print("--OPTIONS--")
    print("1 - check balance")
    print("2 - withdraw money")
    print("3 - log out")
    choice = 0
    while choice != 3:
        choice = int(input('> '))
        if choice == 1:
            print(f"BALANCE: {atm.handle_balance_request()}$")
        elif choice == 2:
            amount = int(input('Enter amount of money to withdrawal: '))
            print(f"-{amount}$\n{atm.handle_withdrawal(amount)}")
    atm.handle_logout()
elif login == 'n':
    print("OK")
