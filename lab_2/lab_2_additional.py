from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color: str = "red", filled: bool = True) -> None:
        self._color = color
        self._filled = filled

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        self._color = color

    @property
    def filled(self) -> bool:
        return self._filled

    @filled.setter
    def filled(self, filled: bool) -> None:
        self._filled = filled

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    def __str__(self) -> str:
        return 'Shape[color={0}, filled={1}]'.format(
            str(self._color),
            str(self._filled))


class Circle(Shape):
    def __init__(self, radius: float = 1.0, color: str = "red",
                 filled: bool = True) -> None:
        super().__init__(color, filled)
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, radius: float) -> None:
        self._radius = radius

    def get_area(self) -> float:
        return math.pi * self._radius**2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def __str__(self) -> str:
        return 'Circle[Shape[color={0}, filled={1}], radius={2}]'.format(
            str(self._color),
            str(self._filled),
            str(self._radius))


class Rectangle(Shape):
    def __init__(self, width: float = 1.0, length: float = 1.0,
                 color: str = "red", filled: bool = True) -> None:
        super().__init__(color, filled)
        self._width = width
        self._length = length

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float) -> None:
        self._width = width

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length) -> None:
        self._length = length

    def get_area(self) -> float:
        return self.width * self.length

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def __str__(self) -> str:
        return 'Rectangle[Shape[color={0}, filled={1}], width={2}, length={3}]'.format(
            str(self._color),
            str(self._filled),
            str(self._width),
            str(self._length))


class Square(Rectangle):
    def __init__(self, side: float = 1.0, color: str = "red", filled: bool = True) -> None:
        super().__init__(side, side, color, filled)
        self.__side = side

    @property
    def side(self) -> float:
        return self.__side

    @side.setter
    def side(self, side) -> None:
        self.__side = side

    def __str__(self) -> str:
        return 'Square[Rectangle[Shape[color={0}, filled={1}], width={2}, length={3}]]'.format(
            str(self._color),
            str(self._filled),
            str(self._width),
            str(self._length))
