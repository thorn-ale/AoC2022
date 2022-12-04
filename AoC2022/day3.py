from dataloader import get_input_data


def main():
    data = get_input_data(3)
    scores = {chr(x):i+1 for i, x in enumerate(list(range(97,123))+list(range(65,91)))}
    bags = [x for x in data.split('\n') if x]
    print(sum([(lambda p1, p2: scores[list(p1.intersection(p2))[0]])(set(list(x[:len(x)//2])), set(list(x[len(x)//2:]))) for x in bags]))
    print(sum([(lambda s1, s2, s3: scores[list(s1.intersection(s2, s3))[0]])(set(list(bags[i])), set(list(bags[i+1])), set(list(bags[i+2]))) for i in range(0, len(bags), 3)]))

if __name__ == '__main__':
    main()

