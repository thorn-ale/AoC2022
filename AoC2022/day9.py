from dataloader import get_input_data
from dataclasses import dataclass
from enum import Enum
from collections import namedtuple
from itertools import product


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

@dataclass
class HeadMove:
    direction: Direction
    step_count: int


def parse_line(line: str) -> HeadMove:
    dir, n = line.split(' ')
    match dir:
        case 'L':
            dir = Direction.LEFT
        case 'R':
            dir = Direction.RIGHT
        case 'U':
            dir = Direction.UP
        case 'D':
            dir = Direction.DOWN
    return HeadMove(dir, int(n))


@dataclass
class Point:
    x: int
    y: int
    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)
    def __sub__(self, p2):
        return Point(self.x - p2.x, self.y - p2.y)
    def __hash__(self) -> int:
        return hash((self.x, self.y))



def get_dir_vec(dir: Direction) -> Point:
    match dir:
        case Direction.LEFT:
            return Point(-1, 0)
        case Direction.RIGHT:
            return Point(1, 0)
        case Direction.UP:
            return Point(0, 1)
        case Direction.DOWN:
            return Point(0, -1)


def clamp(inf: int, val: int, sup: int) -> int:
    return min(sup, max(val, inf))


class Rope:
    def __init__(self, moves: list[HeadMove], nb_nodes: int) -> None:
        self.moves = moves
        self.tail = [Point(0, 0) for _ in range(nb_nodes)]
        self.tail_pos_set = set()
        self.tail_pos_set.add(self.tail[-1])

    def move(self, prev: Point, next: Point) -> Point:
        p = prev - next
        delta = Point(clamp(-1, p.x, 1), clamp(-1, p.y, 1))
        if p == delta:
            return next
        return next + delta

    def play_moves(self):
        for m in self.moves:
            for _ in range(m.step_count):
                self.tail[0] += get_dir_vec(m.direction)
                for j in range(len(self.tail)-1):
                    self.tail[j+1] = self.move(self.tail[j], self.tail[j+1])
                self.tail_pos_set.add(self.tail[-1])
        return len(self.tail_pos_set)


def main():
    data = get_input_data(9)
    head_movments = [parse_line(x) for x in data.split('\n') if x]
    print(Rope(head_movments, 2).play_moves())
    print(Rope(head_movments, 10).play_moves())


if __name__ == '__main__':
    main()

