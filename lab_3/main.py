import abstract_factory as a


def main():
    # Cappuccino
    product = a.CappuccinoFactory().getProductFactory("Cappuccino")
    cappuccino = product.getProduct(a.Customization(0.0, 0.0, 0.0))
    cappuccino.setMilk(100.0)
    cappuccino.setCoffee(0.5)
    cappuccino.setSugar(0.25)
    cappuccino.make()

    print()

    # BlackCoffee
    product = a.BlackCoffeeFactory().getProductFactory("BlackCoffee")
    blackCoffee = product.getProduct(a.Customization(20.0, 1.0, 0.0))
    blackCoffee.setWater(150.0)
    blackCoffee.setCoffee(0.7)
    blackCoffee.make()

    print()

    # Lemonade
    product = a.LemonadeFactory().getProductFactory("Lemonade")
    lemonade = product.getProduct(a.Customization(0.0, 3.5, 1.0))
    lemonade.setWater(150.0)
    lemonade.setSugar(2.5)
    lemonade.setLemoneJuice(5.5)
    lemonade.make()

    print()

    # HotMilk
    product = a.HotMilkFactory().getProductFactory("HotMilk")
    hotMilk = product.getProduct(a.Customization(0.0, 1.5, 0.0))
    hotMilk.setMilk(150.0)
    hotMilk.make()

    print()

    # CocaCola
    product = a.CocaColaFactory().getProductFactory("CocaCola")
    cocaCola = product.getProduct(a.Customization(0.0, 0.0, 50.0))
    cocaCola.setWater(145.0)
    cocaCola.setCoke(5.0)
    cocaCola.make()


if __name__ == "__main__":
    main()