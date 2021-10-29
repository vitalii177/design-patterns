from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Customization:
    extraMilk: float
    sugar: float
    mugSize: float


@dataclass
class Preparation:
    milk: float
    water: float
    sugar: float
    coke: float
    liquidCoffee: float
    addedFlavour: float
    tea: float


class Product(metaclass=ABCMeta):
    @abstractmethod
    def make(self) -> None:
        pass


class Cappuccino(Product):
    def __init__(self, cust) -> None:
        self.cust = cust
        self.prep = Preparation(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def make(self) -> None:
        print(f"Cappuccino is made with {self.prep.milk}g milk, "
              f"{self.prep.sugar}g sugar and {self.prep.liquidCoffee}g coffee")
        print(f"Some customizations {self.cust.extraMilk}g extraMilk, "
              f"{self.cust.sugar}g sugar and {self.cust.mugSize}g mugSize")

    def setMilk(self, milk: float) -> None:
        self.prep.milk = milk

    def setSugar(self, sugar: float) -> None:
        self.prep.sugar = sugar

    def setCoffee(self, coffee: float) -> None:
        self.prep.liquidCoffee = coffee


class BlackCoffee(Product):
    def __init__(self, cust) -> None:
        self.cust = cust
        self.prep = Preparation(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def make(self) -> None:
        print(f"BlackCoffee is made with "
              f"{self.prep.water}g water and {self.prep.liquidCoffee}g coffee")
        print(f"Some customizations {self.cust.extraMilk}g extraMilk, "
              f"{self.cust.sugar}g sugar and {self.cust.mugSize}g mugSize")

    def setWater(self, water: float) -> None:
        self.prep.water = water

    def setCoffee(self, coffee: float) -> None:
        self.prep.liquidCoffee = coffee


class Lemonade(Product):
    def __init__(self, cust) -> None:
        self.cust = cust
        self.prep = Preparation(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def make(self) -> None:
        print(f"Lemonade is made with {self.prep.water}g water, "
              f"{self.prep.sugar}g sugar and {self.prep.addedFlavour}g lemon juice")
        print(f"Some customizations {self.cust.extraMilk}g extraMilk, "
              f"{self.cust.sugar}g sugar and {self.cust.mugSize}g mugSize")

    def setWater(self, water: float) -> None:
        self.prep.water = water

    def setSugar(self, sugar: float) -> None:
        self.prep.sugar = sugar

    def setLemoneJuice(self, lemonJuice: float) -> None:
        self.prep.addedFlavour = lemonJuice


class HotMilk(Product):
    def __init__(self, cust) -> None:
        self.cust = cust
        self.prep = Preparation(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def make(self) -> None:
        print(f"HotMilk is made with {self.prep.milk}g milk")
        print(f"Some customizations {self.cust.extraMilk}g extraMilk, "
              f"{self.cust.sugar}g sugar and {self.cust.mugSize}g mugSize")

    def setMilk(self, milk: float) -> None:
        self.prep.milk = milk


class CocaCola(Product):
    def __init__(self, cust) -> None:
        self.cust = cust
        self.prep = Preparation(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def make(self) -> None:
        print(f"CocaCola is made with {self.prep.water}g water and {self.prep.coke}g coke")
        print(f"Some customizations {self.cust.extraMilk}g extraMilk, "
              f"{self.cust.sugar}g sugar and {self.cust.mugSize}g mugSize")

    def setWater(self, water: float) -> None:
        self.prep.water = water

    def setCoke(self, coke: float) -> None:
        self.prep.coke = coke


class ProductFactory(metaclass=ABCMeta):
    @abstractmethod
    def getProduct(self, customization: Customization) -> Product:
        pass

    @staticmethod
    def getProductFactory(factoryType):
        factory_dict = {
            "Cappuccino": CappuccinoFactory,
            "BlackCoffee": BlackCoffeeFactory,
            "Lemonade": LemonadeFactory,
            "HotMilk": HotMilkFactory,
            "CocaCola": CocaColaFactory
        }
        return factory_dict[factoryType]()


class CappuccinoFactory(ProductFactory):
    def getProduct(self, customization: Customization) -> Cappuccino:
        return Cappuccino(customization)


class BlackCoffeeFactory(ProductFactory):
    def getProduct(self, customization: Customization) -> BlackCoffee:
        return BlackCoffee(customization)


class LemonadeFactory(ProductFactory):
    def getProduct(self, customization: Customization) -> Lemonade:
        return Lemonade(customization)


class HotMilkFactory(ProductFactory):
    def getProduct(self, customization: Customization) -> HotMilk:
        return HotMilk(customization)


class CocaColaFactory(ProductFactory):
    def getProduct(self, customization: Customization) -> CocaCola:
        return CocaCola(customization)
