from dataloader import get_input_data
from functools import reduce


class Pair:
    def __init__(self, l, r) -> None:
        self.left = l
        self.right = r


def compare(val_left, val_right) -> int:
    match val_left, val_right:
        case int(val_left), int(val_right):
            return val_left - val_right
        case list(val_left), list(val_right):
            for x, y in zip(val_left, val_right):
                res = compare(x, y)
                if res:
                    return res
            return len(val_left) - len(val_right)
        case list(val_left), int(val_right):
            return compare(val_left, [val_right])
        case int(val_left), list(val_right):
            return compare([val_left], val_right)


class Packet:
    def __init__(self, pval):
        self.pval = pval

    def __lt__(self, other):
        return compare(self.pval, other.pval) < 0

    def __eq__(self, other):
        return compare(self.pval, other.pval) == 0


def main():
    data = get_input_data(13)
    pairs = [Pair(eval(x.split('\n')[0]), eval(x.split('\n')[1])) for x in data.split('\n\n') if x]
    print(sum([i+1 for i, p in enumerate(pairs) if compare(p.left, p.right)<0]))
    p2 = Packet([[2]])
    p6 = Packet([[6]])
    packets = sorted([Packet(eval(x)) for x in data.split('\n') if x] + [p2] + [p6])
    print(reduce(int.__mul__, [i+1 for i, p in enumerate(packets) if p in [p2,p6]]))

if __name__ == '__main__':
    main()

