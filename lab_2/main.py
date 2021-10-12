import lab_2_additional as f


def main():
    circle = f.Circle()
    print(circle.__str__())
    print("area:", circle.get_area(), "\nperimeter:", circle.get_perimeter(), "\n")

    rectangle = f.Rectangle(2.0, 4.0, "yellow", True)
    print(rectangle.__str__())
    print("area:", rectangle.get_area(), "\nperimeter:", rectangle.get_perimeter(), "\n")

    square = f.Square(5.0, "blue")
    print(square.__str__())
    print("area:", square.get_area(), "\nperimeter:", square.get_perimeter())


if __name__ == "__main__":
    main()
