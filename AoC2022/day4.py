from dataloader import get_input_data


def main():
    data = get_input_data(4)
    print(len(list(filter(
        lambda i: i,
        [(lambda a, b, c, d: set(range(a, b+1)).issubset(set(range(c, d+1))) or set(range(c, d+1)).issubset(set(range(a, b+1)))) 
            (int(y.split(',')[0].split('-')[0]), int(y.split(',')[0].split('-')[1]), int(y.split(',')[1].split('-')[0]), int(y.split(',')[1].split('-')[1])) 
            for y in data.split('\n') if y]))))
    print(len(list(filter(
        lambda i: i, 
        [(lambda a, b, c, d: len(set(range(a, b+1)).intersection(set(range(c, d+1)))) > 0 )
            (int(y.split(',')[0].split('-')[0]), int(y.split(',')[0].split('-')[1]), int(y.split(',')[1].split('-')[0]), int(y.split(',')[1].split('-')[1])) 
            for y in data.split('\n') if y]))))


if __name__ == '__main__':
    main()

