from dataloader import get_input_data


# A = Rock  = X
# B = Paper = Y
# C = Scissors = Z
def get_score_1(line):
    X = 1 # rock
    Y = 2 # paper
    Z = 3 # scissors
    WIN = 6
    LOSS = 0
    DRAW = 3
    i, j = line.split(' ')
    match (i, j):
        case ('A', 'X'):
            return eval(j) + DRAW # draw
        case ('A', 'Y'):
            return eval(j) + WIN # win
        case ('A', 'Z'):
            return eval(j) + LOSS #loss
        case ('B', 'X'):
            return eval(j) + LOSS #loss
        case ('B', 'Y'):
            return eval(j) + DRAW #draw
        case ('B', 'Z'):
            return eval(j) + WIN #win
        case ('C', 'X'):
            return eval(j) + WIN #win
        case ('C', 'Y'):
            return eval(j) + LOSS #loss
        case ('C', 'Z'):
            return eval(j) + DRAW #draw
        case _:
            print(f'Pattern ({i}, {j}) unknown')

# A = Rock  = X
# B = Paper = Y
# C = Scissors = Z
def get_score_2(line):
    WIN = 6
    LOSS = 0
    DRAW = 3
    ROCK = 1 # rock
    PAPER = 2 # PAPER
    SCIS = 3 # scissors
    i, j = line.split(' ')
    match (i, j):
        case ('A', 'X'): # need loose against rock
            return SCIS + LOSS
        case ('A', 'Y'): # need draw against rock
            return ROCK + DRAW
        case ('A', 'Z'): # need win against rock
            return PAPER + WIN
        case ('B', 'X'): # need loose against paper
            return ROCK + LOSS
        case ('B', 'Y'): # need draw against paper
            return PAPER + DRAW
        case ('B', 'Z'): # need win against paper
            return SCIS + WIN 
        case ('C', 'X'): # need loose against scissors
            return PAPER + LOSS 
        case ('C', 'Y'): # need draw against scissors
            return SCIS + DRAW
        case ('C', 'Z'): # need win against scissors
            return ROCK + WIN
        case _:
            print(f'Pattern ({i}, {j}) unknown')


def main():
    data = get_input_data(2)
    print(sum([get_score_1(x) for x in data.split('\n') if x]))
    print(sum([get_score_2(x) for x in data.split('\n') if x]))


if __name__ == '__main__':
    main()

