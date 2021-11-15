from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from cryptography.fernet import Fernet
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


class CreditCardDecorator:
    def __init__(self, decorated_card):
        self.decorated_card = decorated_card

    def add_contactless_chip(self):
        self.decorated_card.contactless_chip = True
        return self.decorated_card


class GoldenCreditCard(CreditCardDecorator):
    def __init__(self, decorated_card):
        super(GoldenCreditCard, self).__init__(decorated_card)

    def add_contactless_chip(self):
        super(GoldenCreditCard, self).add_contactless_chip()
        print("Contactless chip has added to GoldenCreditCard")


class CorporateCreditCard(CreditCardDecorator):
    def __init__(self, decorated_card):
        super(CorporateCreditCard, self).__init__(decorated_card)

    def add_contactless_chip(self):
        super(CorporateCreditCard, self).add_contactless_chip()
        print("Contactless chip has added to CorporateCreditCard")


# The client
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

golden_credit_card = GoldenCreditCard(credit_card)
golden_credit_card.add_contactless_chip()

corporate_credit_card = CorporateCreditCard(credit_card)
corporate_credit_card.add_contactless_chip()
