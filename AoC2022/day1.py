from dataloader import get_input_data

def main():
    data = get_input_data(1)
    accumulators = sorted([sum([int(y) for y in x.split('\n')])for x in data.split('\n\n')], reverse=True)
    print(accumulators[0])
    print(sum(accumulators[:3]))


if __name__ == '__main__':
    main()

