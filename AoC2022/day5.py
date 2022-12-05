import re
from dataclasses import dataclass
from dataloader import get_input_data


def parse_stack(data: str) -> dict[int, list[str]]:
    print(data)
    result = {i:[] for i in range (1, 10)}
    raw_stack = data.split('\n')
    raw_stack.reverse()
    for line in raw_stack:
        if line.startswith(' 1'): continue
        for i in range(9):
            crate_id = line[i*4+1]
            if crate_id != ' ':
                result[i+1].append(crate_id)
    return result


@dataclass
class Intstruction:
    qt: int
    src: int
    dst: int

def parse_orders(data: str) -> list[Intstruction]:
    return [Intstruction(*[int(x) for x in re.findall('[0-9]+', line)]) for line in data.split('\n') if line.startswith('move')]

def play_order(order: Intstruction, stacks: dict[int, list[str]]) -> dict[int, list[str]]:
    for _ in range(order.qt):
        temp = stacks[order.src].pop()
        stacks[order.dst].append(temp)
    return stacks

def play_order_p2(order: Intstruction, stacks: dict[int, list[str]]) -> dict[int, list[str]]:
    temp = stacks[order.src][-order.qt:]
    stacks[order.dst] += temp
    for _ in range(order.qt):
        stacks[order.src].pop()
    return stacks


def main():
    data = get_input_data(5)
    stacks = parse_stack(data.split('move')[0].strip())
    stacks2 = parse_stack(data.split('move')[0].strip())
    orders = parse_orders(data)
    for o in orders:
        stacks = play_order(o, stacks)
        stacks2 = play_order_p2(o, stacks2)

    print('result 1: ')
    acc = ''
    for k, v in stacks.items():
        acc += v[-1]
        print(f'{k} => {v}')
    print(acc)

    print('result 2: ')
    acc2 = ''
    for k, v in stacks2.items():
        acc2 += v[-1]
        print(f'{k} => {v}')
    print(acc2)


if __name__ == '__main__':
    main()

