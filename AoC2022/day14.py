from dataloader import get_input_data
from dataclasses import dataclass
from PIL import Image

ROCK = '#'
SAND = 'O'
AIR = '.'
START = '+'

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


def part1():
    data = get_input_data(14)
    rock_pos = [[Point(int(y.split(',')[0]), int(y.split(',')[1])) for y in x.split(' -> ')] for x in data.split('\n') if x]

    cave = {}
    max_depth = max([y.y for x in rock_pos for y in x])
    
    for line in rock_pos:
        for i in range(1, len(line)):
            start = line[i-1]
            end = line[i]
            if start.x == end.x:
                sy = min(start.y, end.y)
                ey = max(start.y, end.y)
                for j in range(sy, ey+1):
                    cave[Point(start.x, j)] = ROCK

            if start.y == end.y:
                sx = min(start.x, end.x)
                ex = max(start.x, end.x)
                for j in range(sx, ex+1):
                    cave[Point(j, start.y)] = ROCK

    sand_start = Point(500,0)
    cave[sand_start] = START
    
    down = Point(0, 1)
    down_left = Point(-1, 1)
    down_right = Point(1, 1)
    nb_sand = 0
    full = False
    
    while not full:
        current_sand_pos = sand_start
        prev_nb_sand = nb_sand
        while current_sand_pos.y < max_depth+1:
            try_down = current_sand_pos + down
            try_dl = current_sand_pos + down_left
            try_dr = current_sand_pos + down_right
            # try go down (x, y+1)
            if not try_down in cave.keys():
                current_sand_pos = try_down
            # else down left diagonaly(x-1, y+1)
            elif not try_dl in cave.keys():
                current_sand_pos = try_dl
            # else down right diagonaly(x+1, y+1)
            elif not try_dr in cave.keys():
                current_sand_pos = try_dr
            else:
                nb_sand += 1
                cave[current_sand_pos] = SAND
                break
        if nb_sand == prev_nb_sand: 
            full = True
    
    print(nb_sand)


def view_step(cave, depth, width):
    img = Image.new('RGB', (width, depth+1))
    sand = (255,186,3)
    rock = (0,0,0)
    air = (255,255,255)
    for y in range(width):
        for x in range(depth+1):
            value = cave.get(Point(y, x), '.')
            match value:
                case '#':
                    img.putpixel((y,x), rock)
                case 'O':
                    img.putpixel((y,x), sand)
                case '.':
                    img.putpixel((y,x), air)
    return img

def part2():
    data = get_input_data(14)
    rock_pos = [[Point(int(y.split(',')[0]), int(y.split(',')[1])) for y in x.split(' -> ')] for x in data.split('\n') if x]

    cave = {}
    max_depth = max([y.y for x in rock_pos for y in x])
    max_width = int(max([y.x for x in rock_pos for y in x])*1.5)
    
    for line in rock_pos:
        for i in range(1, len(line)):
            start = line[i-1]
            end = line[i]
            if start.x == end.x:
                sy = min(start.y, end.y)
                ey = max(start.y, end.y)
                for j in range(sy, ey+1):
                    cave[Point(start.x, j)] = ROCK

            if start.y == end.y:
                sx = min(start.x, end.x)
                ex = max(start.x, end.x)
                for j in range(sx, ex+1):
                    cave[Point(j, start.y)] = ROCK

    for i in range(max_width):
        cave[Point(i, max_depth+2)] = ROCK

    max_depth += 2

    sand_start = Point(500,0)
    
    down = Point(0, 1)
    down_left = Point(-1, 1)
    down_right = Point(1, 1)
    nb_sand = 0
    full = False
    
    while not full:
        current_sand_pos = sand_start
        while current_sand_pos.y < max_depth+1:
            try_down = current_sand_pos + down
            try_dl = current_sand_pos + down_left
            try_dr = current_sand_pos + down_right
            # try go down (x, y+1)
            if not try_down in cave.keys():
                current_sand_pos = try_down
            # else down left diagonaly(x-1, y+1)
            elif not try_dl in cave.keys():
                current_sand_pos = try_dl
            # else down right diagonaly(x+1, y+1)
            elif not try_dr in cave.keys():
                current_sand_pos = try_dr
            else:
                nb_sand += 1
                cave[current_sand_pos] = SAND
                break
        if current_sand_pos == sand_start: 
            full = True
    
    view_step(cave, max_depth, max_width).save('./debug/result.png')
    print(nb_sand)


if __name__ == '__main__':
    part1()
    part2()
