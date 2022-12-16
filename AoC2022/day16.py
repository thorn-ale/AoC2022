from dataloader import get_input_data
from dataclasses import dataclass
import math
import re
from functools import cache


@dataclass
class Valve:
    name: str
    rate: int
    links: list['str']

    def score(self) -> int:
        return self.rate * len(self.links)


def parse_data(data: str):
    vs = re.findall(r'[A-Z]{2}', data)
    rate = int(re.findall(r'\d+', data)[0])
    return Valve(vs[0], rate, vs[1:])


@dataclass
class WalkParams:
    current: str
    valves: dict[str, Valve]
    dists: dict[str:[dict[str,int]]]
    rt: int
    elephant: bool = False

    def __hash__(self) -> int:
        hv = frozenset([(k,v.name) for k,v in self.valves.items()])
        return hash((self.current, hv, self.rt, self.elephant))


@cache
def walk(wp: WalkParams) -> int:
    res = walk(WalkParams('AA', wp.valves, wp.dists, 26)) if wp.elephant else 0
    for v in wp.valves.keys():
        move = wp.rt - wp.dists[wp.current][v] - 1
        if move >= 0:
            res = max(res, wp.valves[v].rate * move + walk(WalkParams(
                v, {k: v2 for k, v2 in wp.valves.items() if k != v}, wp.dists, move, wp.elephant)))
    return res


def main():
    data = get_input_data(16)
    valves = [parse_data(x) for x in data.split('\n') if x]
    dists = {v.name:{x.name: 1 if x.name in v.links else 0 if x.name == v.name else math.inf for x in valves} for v in valves}
    names = [x.name for x in valves]
    valves = {v.name: v for v in valves if v.rate > 0}
    for i in names:
        for j in names:
            for k in names:
                dists[j][k] = min(dists[j][k], dists[j][i] + dists[i][k])

    print(walk(WalkParams('AA', valves, dists, 30)))
    print(walk(WalkParams('AA', valves, dists, 26, True)))


if __name__ == '__main__':
    main()

