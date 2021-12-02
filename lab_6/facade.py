"""................................Inventory Subsystem......................................"""


class Product:
    def __init__(self, product_id: int, price: float, type: str):
        self.id = product_id
        self.price = price
        self.type = type

    def add_product(self, id: int, price: float, type: str) -> None:
        self.id = id
        self.price = price
        self.type = type
        print(f"Product with id={self.id} is added")

    def update_product(self):
        return f"Product[id={self.id}, price={self.price}, type={self.type}]"


class Stock:
    def __init__(self, stock_id: int):
        self.id = stock_id
        self.amount = 0
        self.products = []

    def select_stock_item(self, product) -> None:
        for i in range(len(self.products)):
            if product.id == self.products[i]['id']:
                print(f"Stock[id={self.id}, amount={self.amount}, {product.update_product()}]")

    def update_stock(self, product: Product, amount: int):
        self.amount = amount
        product.add_product(product.id, product.price, product.type)
        self.products.append({"id": product.id, "price": product.price, "type:": product.type})


""".............................Order Process Subsystem....................................."""


class ShoppingCart:
    def __init__(self, stock: Stock):
        self.stock = stock
        self.total = 0.0
        self.items = {}

    def add_item(self, product_price) -> None:
        self.total += (self.stock.amount * product_price)

    def update_amount(self, stock_id, new_amount: float) -> None:
        self.items = {stock_id: new_amount}

    def checkout(self, cash_paid: float):
        if cash_paid >= self.total:
            return cash_paid - self.total
        return 'Cash paid not enough'


class Order:
    def __init__(self, order_id: int):
        self.id = order_id
        self.shopping_cart = None

    def create_order(self, stock, product_price):
        self.shopping_cart = ShoppingCart(stock)
        self.shopping_cart.add_item(product_price)

    def edit_order(self, stock_id, amount, shopping_cart: ShoppingCart):
        shopping_cart.update_amount(stock_id, amount)


""".............................Shipment Subsystem........................................"""


class Shipment:
    def __init__(self, order: Order, provider):
        self.order = order
        self.provider = provider

    def create_shipment(self, provider_id: int, product_price: float, stock: Stock) -> None:
        for i in range(len(self.provider.providers)):
            if provider_id == self.provider.id:
                self.order.create_order(stock, product_price)
                print(f"SHIPMENT. Your order with id={self.order.id} has been delivered")

    def add_provider(self, provider_id: int):
        self.provider.add_provider(provider_id)


class ShipmentProvider:
    def __init__(self, id: int, name: str, phone_number: str):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.providers = []

    def add_provider(self) -> None:
        print(f"Provider with id={self.id} has been added")
        self.providers.append({'id': self.id,
                               'name': self.name,
                               'email': self.phone_number})


"""................................Payment Subsystem......................................"""


class Payment:
    def __init__(self):
        self.card_details = {}

    def add_card_details(self, card_number, money) -> None:
        self.card_details = {'card_number': card_number, 'balance': money}

    def verify_payment(self, shopping_cart: ShoppingCart):
        return shopping_cart.checkout(self.card_details['balance'])


"""......................................................................................."""


class OrderFacade:
    def __init__(self, stock: Stock, shipment_provider: ShipmentProvider, shopping_cart: ShoppingCart):
        self.shipment_provider = shipment_provider
        self.stock = stock
        self.shopping_cart = shopping_cart

    def do_operation(self, order_id, provider_id, product_price) -> None:
        order = Order(order_id)
        shipment = Shipment(order, self.shipment_provider)
        order.create_order(self.stock, product_price)
        shipment.create_shipment(provider_id, self.shopping_cart.total, self.stock)
        print(f"You must pay {product_price}$")


class Customer:
    def __init__(self, payment: Payment):
        self.payment = payment

    def order_item(self, order_id, provider_id, product_price, order_facade: OrderFacade) -> None:
        print('You have to input you card number OR input [x] to exit:')
        while True:
            card_number = str(input('> '))
            if card_number == self.payment.card_details['card_number']:
                break
            elif card_number == 'x':
                return
        if self.payment.verify_payment(order_facade.shopping_cart) >= product_price:
            order_facade.do_operation(order_id, provider_id, product_price)
            print(f"Balance: {self.payment.card_details['balance']}$")
            self.payment.card_details['balance'] -= product_price
            print(f"-{product_price}$\nBalance: {self.payment.card_details['balance']}$")
        else:
            print(f"You must pay {product_price}$, you lack {product_price-self.payment.card_details['balance']}$")


# The client code
product1 = Product(product_id=1, price=12.0, type='apple')
product2 = Product(product_id=2, price=34.0, type='milk')

stock = Stock(stock_id=1)
stock.update_stock(product=product1, amount=10)
stock.select_stock_item(product=product1)
stock.update_stock(product=product2, amount=34)
stock.select_stock_item(product=product2)

shopping_cart = ShoppingCart(stock=stock)

shipment_provider = ShipmentProvider(id=1, name='John', phone_number='134-34-234')
shipment_provider.add_provider()
order_facade = OrderFacade(stock=stock, shipment_provider=shipment_provider, shopping_cart=shopping_cart)

payment = Payment()
payment.add_card_details(card_number='2424-3452-2345-4635', money=354.4)
print(payment.card_details)

customer = Customer(payment=payment)
customer.order_item(order_id=1,
                    provider_id=shipment_provider.id,
                    product_price=product1.price+product2.price,
                    order_facade=order_facade)
