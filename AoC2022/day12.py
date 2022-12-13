from dataloader import get_input_data
from collections import deque
import math


def search_pos(hmap, width, heigt, target):
    for y in range(heigt):
        for x in range(width):
            if hmap[y][x] == target:
                return y,x


def find_path(hmap, starts, height, width):
    distances = {}
    visited = deque([(0, s) for s in starts])

    while len(visited) > 0:
        t, p = visited.popleft()
        if p in distances.keys():
            continue
        distances[p] = t
        for n_y, n_x in [(p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1)]:
            if n_y < 0 or n_y >= height or n_x < 0 or n_x >= width:
                continue
            elv = hmap[p[0]][p[1]]
            if elv == 'S':
                elv = 'a'
            if elv == 'E':
                elv = 'z'
            n_elv = hmap[n_y][n_x]
            if n_elv == 'S':
                n_elv = 'a'
            if n_elv == 'E':
                n_elv = 'z'
            if ord(n_elv) - ord(elv) > 1:
                continue
            visited.append((t+1, (n_y, n_x)))
    return distances


def main():
    data = get_input_data(12)
    hmap = [[x for x in y] for y in data.split('\n') if y]
    width = len(hmap[0])
    height = len(hmap)
    start_pos = search_pos(hmap, width, height, 'S')
    target = search_pos(hmap, width, height, 'E')
    distances = find_path(hmap, [start_pos], height, width)
    print(distances[target])
    starts = [(y, x) for y in range(height) for x in range(width) if hmap[y][x] == 'a']
    n_dist = find_path(hmap, starts, height, width).get(target, math.inf)
    print(n_dist)
    


if __name__ == '__main__':
    main()

