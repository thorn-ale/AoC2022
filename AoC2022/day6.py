from dataloader import get_input_data


def first_marker(data, size):
    acc = ''
    for i, char in enumerate(data):
        if not ord(char) in range(ord('a'),ord('z')+1):
            continue
        acc += char
        if len(acc) >= size and len(set(acc[-size:])) == size:
            return (i+1, acc[-size:], set(acc[-size:]))
                

def main():
    data = get_input_data(6)
    print(first_marker(data, 4))
    print(first_marker(data, 14))


if __name__ == '__main__':
    main()

