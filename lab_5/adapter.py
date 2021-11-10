from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from cryptography.fernet import Fernet
from functools import wraps
import random


class ICreditCard(metaclass=ABCMeta):
    @abstractmethod
    def give_details(self, *args) -> dict:
        pass


class CreditCard(ICreditCard):
    def __init__(self, client: str, account_number: str, credit_limit: float,
                 grace_period: int):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = ""
        self.key = Fernet.generate_key()

    @property
    def cvv(self):
        return self._decrypt(self._cvv)

    @cvv.setter
    def cvv(self, cvv):
        self._cvv = self._encrypt(cvv)
        print(f"encrypted: {self._cvv}")

    def give_details(self, *args) -> dict:
        args = {'client': self.client,
                'account_number': self.account_number,
                'credit_limit': self.credit_limit,
                'grace_period': self.grace_period,
                'cvv': self._decrypt(self._cvv)}
        return args

    def _encrypt(self, value: str):
        return Fernet(self.key).encrypt(value.encode())

    def _decrypt(self, value):
        return Fernet(self.key).decrypt(value).decode()


class BankInfo:
    def __init__(self, bank_name: str, holder_name: str):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = []
        self.credit_history = {'transaction_list': []}

    def transaction_list(self, account_number: str):
        for i in range(len(self.accounts_number)):
            if self.accounts_number[i] == account_number:
                self.credit_history['transaction_list'].append(self.accounts_number[i])
        return self.credit_history['transaction_list']


@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phone_number: str
    email: str


class BankCustomer:
    def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
        self._personal_info = personal_info
        self.bank_details = bank_details

    @property
    def personal_info(self):
        return self._personal_info

    @personal_info.setter
    def personal_info(self, personal_info: PersonalInfo):
        self._personal_info = personal_info

    def give_details(self, *args) -> dict:
        args = {'bank_name': self.bank_details.bank_name,
                'holder_name': self.bank_details.holder_name,
                'accounts_number': self.bank_details.accounts_number,
                'credit_history': self.bank_details.credit_history}
        return args


class CreditCardDecorator(ICreditCard):
    _credit_card: ICreditCard = None

    def __init__(self, credit_card: ICreditCard):
        self._credit_card = credit_card

    @property
    def credit_card(self):
        return self._credit_card

    def give_details(self, *args) -> dict:
        return self._credit_card.give_details()


def calculate_tax(fn):
    @wraps(fn)
    def wrapper(self, cash: float, account_number: str, account):
        tax = 0.02
        return fn(self, cash * (1 - tax), account_number, account)
    return wrapper


class Account:
    def __init__(self):
        self.__cash = 0.0

    @property
    def cash(self):
        return self.__cash

    @cash.setter
    def cash(self, cash):
        self.__cash = cash

    def check_money(self) -> str:
        return f"There is {self.__cash}$ in your account!"


class GoldenCreditCard(CreditCardDecorator):
    @calculate_tax
    def transfer_cash(self, cash: float, account_number: str, account: Account):
        choice = str(input("PDV=2%, Do you want to transfer your cash [y/n]: "))
        if choice == 'y':
            cvv = str(input('ENTER YOR CVV CODE, PLEASE: '))
            if cvv == self.credit_card.cvv:
                report = {'account_number': account_number,
                          'cash': cash}
                account.cash = cash
                account.check_money()
                return f"Your cash had been transferred successfully! {report}"
            else:
                return"Sorry, you have entered incorrect CVV code!"
        elif choice == 'n':
            return "Thank you for your choice, BYE!"


def get_discount(fn):
    @wraps(fn)
    def wrapper(self, check_to_pay: float, account):
        discount = 0.05
        if check_to_pay >= 500:
            print(f"You made a purchase more than 500$ so you have a DISCOUNT 5%")
            check_to_pay = check_to_pay * (1 - discount)
        return fn(self, check_to_pay, account)
    return wrapper


class CorporateCreditCard(CreditCardDecorator):
    @get_discount
    def pay_bill(self, check_to_pay: float, account: Account):
        if account.cash >= check_to_pay:
            account.cash -= check_to_pay
            return f"You paid the bill successfully -{check_to_pay}$"
        else:
            return "Sorry, You lack money in your account!"


# The client
print("ADAPTER DESIGN PATTERN")
credit_card = CreditCard(client='Julia', account_number='123-4-5678-8910-1-1',
                         credit_limit=1500.0, grace_period=50)
credit_card.cvv = '235'
print(f"decrypted: {credit_card.cvv}")
print(credit_card.give_details(credit_card))

bank = BankInfo(bank_name='ProCredit Bank', holder_name='Mr Henry Jones')

client_info = PersonalInfo(id=0, name='Julia', address='821 Eugene Trail',
                           phone_number='(440) 961-3559 x419', email='julia@gmail.com')
client = BankCustomer(personal_info=client_info, bank_details=bank)

bank.accounts_number.append(credit_card.account_number)
bank.transaction_list(credit_card.account_number)
print(client.give_details(client))

print("\nDECORATOR DESIGN PATTERN")

account = Account()

golden_card = GoldenCreditCard(credit_card)
cash = float(input('Enter amount of cash for transferring: '))
print(golden_card.transfer_cash(cash=cash, account_number=credit_card.account_number, account=account))

corporate_card = CorporateCreditCard(credit_card)
check = random.randint(5, 1000)
print(f"You MUST PAY THE BILL {check}$")
print(corporate_card.pay_bill(check_to_pay=check, account=account))
print(account.check_money())
