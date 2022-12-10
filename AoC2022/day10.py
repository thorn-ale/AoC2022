from dataloader import get_input_data

class Tokens:
    noop = 'noop'
    addx = 'addx'

def manage_cycle(cycle, x_val, crt, res):
    good_cycles = list(range(20,221,40))
    if cycle%40 in [x_val-1, x_val, x_val+1]:
        crt.append('#')
    else:
        crt.append(' ')
    cycle += 1
    if not cycle%40:
        crt.append('\n')
    if cycle in good_cycles:
        res.append(x_val*cycle)
    return cycle, x_val, crt, res

def interpretor(programm):
    x_val = 1
    cycle = 0
    res = []
    crt = []
    for instr in programm:
        if Tokens.noop in instr:
            cycle, x_val, crt, res = manage_cycle(cycle, x_val, crt, res)
        elif Tokens.addx in instr:
            cycle, x_val, crt, res = manage_cycle(cycle, x_val, crt, res)
            cycle, x_val, crt, res = manage_cycle(cycle, x_val, crt, res)
            x_val += int(instr.split(' ')[1])
    return sum(res), ''.join(crt)


def main():
    data = get_input_data(10)
    val, display = interpretor(data.split('\n'))
    print(val)
    print()
    print(display)


if __name__ == '__main__':
    main()

