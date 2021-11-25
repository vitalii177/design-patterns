from abc import ABCMeta, abstractmethod
from itertools import product


class Piece(metaclass=ABCMeta):
    def __init__(self, position: list, color: str, move_rule):
        self.position = position
        self.color = color
        self.move_rule = move_rule
        self.number_of_moves = 0

    @abstractmethod
    def move(self, new_position: list) -> dict:
        pass

    @abstractmethod
    def print_info(self) -> None:
        pass

    @staticmethod
    def check_position_range(position: list):
        x, y = position[0]
        if 0 <= x <= 8 and 0 <= y < 8:
            return True
        else:
            return False


class Knight(Piece):
    def __init__(self, position: list, color: str, move_rule):
        super().__init__(position, color, move_rule)

    def move(self, new_position) -> dict:
        if str(new_position)[1:-1] in str(self.move_rule.get_all_moves())[1:-1] \
                and self.check_position_range(self.position):
            self.number_of_moves += 1
            return {self.color + "Knight": f"{str(self.position)[1:-1]} -> {str(new_position)[1:-1]}"}

    def print_info(self) -> None:
        print(f'Knight[position={str(self.position)[1:-1]}, color={self.color}]')


class Bishop(Piece):
    def __init__(self, position: list, color: str, move_rule):
        super().__init__(position, color, move_rule)

    def move(self, new_position: list) -> dict:
        if str(new_position)[1:-1] in str(self.move_rule.get_all_moves())[1:-1] \
                and self.check_position_range(self.position):
            self.number_of_moves += 1
            return {self.color + "Bishop": f"{str(self.position)[1:-1]} -> {str(new_position)[1:-1]}"}

    def print_info(self) -> None:
        print(f'Bishop[position={str(self.position)[1:-1]}, color={self.color}]')


class MoveRule(metaclass=ABCMeta):
    def __init__(self, position: list):
        self.position = position

    @abstractmethod
    def get_all_moves(self) -> list:
        pass


class KnightMove(MoveRule):
    def __init__(self, position: list):
        super().__init__(position)

    def get_all_moves(self) -> list:
        x, y = self.position[0]
        moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
        moves = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
        return moves


class BishopMove(MoveRule):
    def __init__(self, position: list):
        super().__init__(position)

    def get_all_moves(self) -> list:
        x, y = self.position[0]
        moves = []
        directions = [
            zip(range(x+1, 8), range(y-1, -1, -1)),
            zip(range(x+1, 8), range(y+1, 8)),
            zip(range(x-1, -1, -1), range(y-1, -1, -1)),
            zip(range(x-1, -1, -1), range(y+1, 8))
        ]
        for direction in directions:
            for new_x, new_y in direction:
                moves.append((new_x, new_y))
        return moves


# The client code
knight_move = KnightMove(position=[(1, 0)])
knight = Knight(position=knight_move.position, color='White', move_rule=knight_move)
knight.print_info()
print(f"Available moves: {knight_move.get_all_moves()}")
coord_x = int(input('x > '))
coord_y = int(input('y > '))
print(knight.move([(coord_x, coord_y)]))
print("----------------------------------------------------------------------------")
bishop_move = BishopMove(position=[(2, 7)])
bishop = Bishop(position=bishop_move.position, color='Black', move_rule=bishop_move)
bishop.print_info()
print(f"Available moves: {bishop_move.get_all_moves()}")
coord_x = int(input('x > '))
coord_y = int(input('y > '))
print(bishop.move([(coord_x, coord_y)]))
