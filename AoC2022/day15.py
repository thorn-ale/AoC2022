from dataloader import get_input_data
from dataclasses import dataclass
import re
from z3 import *


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

def dist(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x)+abs(p1.y - p2.y)


@dataclass
class Reading:
    sensor: Point
    beacon: Point

    def sensor_range(self) -> int:
        return dist(self.sensor, self.beacon)

    def __repr__(self) -> str:
        return f'{self.sensor} -> {self.beacon}'

def parse_reading(line: str) -> Reading:
    coords = [int(x) for x in re.findall(r'-?\d+', line)]
    return Reading(Point(coords[0], coords[1]), Point(coords[2], coords[3]))


def part1():
    data = get_input_data(15)
    readings = [parse_reading(x) for x in data.split('\n') if x]
    x_max = max([r.beacon.x for r in readings]) + max([r.sensor_range() for r in readings])
    x_min = min([r.beacon.x for r in readings]) - max([r.sensor_range() for r in readings])
    target_y = 2000000
    nb = 0
    beacons = set([x.beacon for x in readings])
    
    for x in range(x_min, x_max):
        in_range = False
        p = Point(x, target_y)
        for i, r in enumerate(readings):
            d = dist(p, r.sensor)
            if d <= r.sensor_range():
                in_range = True
                break
        if in_range and p not in beacons:
            nb += 1
    print(nb)


def part2():
    data = get_input_data(15)
    readings = [parse_reading(x) for x in data.split('\n') if x]
    limit = 4000000
    s = Solver()
    x, y = Ints('x, y')
    s.add(x >= 0)
    s.add(y >= 0)
    s.add(x <= limit)
    s.add(y <= limit)

    def Abs(x):
        return If( x >= 0, x, -x)

    for r in readings:
        s.add(Abs(x - r.sensor.x) + Abs(y - r.sensor.y) > r.sensor_range())
        s.add(And(x != r.beacon.x, y != r.beacon.y))
    
    assert s.check() == sat
    res = s.model()
    print(res[x].as_long() * limit + res[y].as_long())


if __name__ == '__main__':
    part1()
    part2()

