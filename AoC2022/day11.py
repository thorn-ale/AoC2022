from dataloader import get_input_data
from dataclasses import dataclass
from functools import reduce
import re


@dataclass
class Monkey:
    index: int
    items: list[int]
    operation: str
    test_and_throw: tuple[int, int, int]
    nb_inspected_items: int = 0

    def turn(self, modval: int | None = None) -> list[tuple[int, int]]:
        res = []
        for it in self.items:
            wl = (lambda old: eval(self.operation))(it)
            self.nb_inspected_items += 1
            if modval == None:
                wl = wl // 3
            else:
                wl = wl % modval
            dest = (lambda x: self.test_and_throw[0] if not x % self.test_and_throw[1] else self.test_and_throw[2])(wl)
            res.append((wl, dest))
        self.items = []
        return res

    def receive_item(self, item: int):
        self.items.append(item)

    def __repr__(self) -> str:
        return f'{self.index}, {self.items}, {self.nb_inspected_items}'


def parse_monkeys(data: list[str]) -> dict[int,Monkey]:
    return {int(re.findall('\d+', data[i])[0]) : Monkey(
                int(re.findall('\d+', data[i])[0]),
                [int(x) for x in re.findall('\d+', data[i+1])],
                data[i+2].split('=')[-1],
                (int(re.findall("\d+", data[i+4])[0]), int(re.findall("\d+", data[i+3])[0]), int(re.findall("\d+", data[i+5])[0]))
            )
        for i in range(0, len(data), 6)}


def part1(data):
    m_dict = parse_monkeys([x for x in data.split('\n') if x.strip()])
    monkeys = sorted(m_dict.values(), key= lambda m: m.index)
    for _ in range(20):
        
        for m in monkeys:
            results = m.turn()
            for item, dest in results:
                m_dict[dest].receive_item(item)

    print(reduce(int.__mul__,sorted([m.nb_inspected_items for m in monkeys])[-2:]))


def part2(data):
    m_dict = parse_monkeys([x for x in data.split('\n') if x.strip()])
    monkeys = sorted(m_dict.values(), key= lambda m: m.index)
    mm = reduce(int.__mul__,[m.test_and_throw[1] for m in monkeys])
    for _ in range(10000):
        
        for m in monkeys:
            results = m.turn(mm)
            for item, dest in results:
                m_dict[dest].receive_item(item)

    print(reduce(int.__mul__,sorted([m.nb_inspected_items for m in monkeys])[-2:]))


def main():
    data = get_input_data(11)
    part1(data)
    part2(data)
    



if __name__ == '__main__':
    main()

