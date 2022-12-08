from dataloader import get_input_data


def is_visible(grid, width, height, x, y):
    if x == 0 or y == 0 or y == height-1 or x == width-1:
        return True
    left = grid[y][:x]
    right = grid[y][x+1:]
    up = [f[x] for f in grid[:y]]
    down = [f[x] for f in grid[y+1:]]
    curr_tree = grid[y][x]
    return all([curr_tree > t for t in left]) or all([curr_tree > t for t in right]) or all([curr_tree > t for t in up]) or all([curr_tree > t for t in down])


def d_score(curr_tree, other_trees):
    score = 0
    for ot in other_trees:
        if ot < curr_tree:
            score += 1
        else:
            score += 1
            break
    return score


def score(grid, x, y):
    curr_tree = grid[y][x]
    left = grid[y][:x]
    left.reverse()
    right = grid[y][x+1:]
    up = [f[x] for f in grid[:y]]
    up.reverse()
    down = [f[x] for f in grid[y+1:]]
    return d_score(curr_tree, left) * d_score(curr_tree, right) * d_score(curr_tree, up) * d_score(curr_tree, down)
    


def main():
    data = get_input_data(8)
    grid = [[int(y) for y in list(x)] for x in data.split('\n') if x.strip()]
    height = len(grid)
    width = len(grid[0])
    print(len([x for y in range(height) for x in range(width) if is_visible(grid, width, height, x, y)]))
    print(max([score(grid, x, y) for y in range(height) for x in range(width)]))


if __name__ == '__main__':
    main()

