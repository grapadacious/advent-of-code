import signal
import sys

def count_visible_tb(input, grid):
    total = 0

    for i in range(len(input[0])):
        t_total = 0
        b_total = 0

        t_max = -1
        b_max = -1

        t = 0
        b = len(input) - 1
        while (t < len(input)):
            t_tree = int(input[t][i])
            b_tree = int(input[b][i])

            if t_tree > t_max:
                t_max = t_tree

                if not grid[t][i]:
                    t_total += 1
                    grid[t][i] = True

            if b_tree > b_max:
                b_max = b_tree

                if not grid[b][i]:
                    b_total += 1
                    grid[b][i] = True

            t += 1
            b -= 1

        total += t_total + b_total

    return total

def count_visible_lr(input, grid):
    total = 0

    for i in range(len(input)):
        l_total = 0
        r_total = 0

        l_max = -1
        r_max = -1

        l = 0
        r = len(input[i]) - 1
        while (l < len(input[i])):
            l_tree = int(input[i][l])
            r_tree = int(input[i][r])

            if l_tree > l_max:
                l_max = l_tree

                if not grid[i][l]:
                    l_total += 1
                    grid[i][l] = True

            if r_tree > r_max:
                r_max = r_tree
                
                if not grid[i][r]:
                    r_total += 1
                    grid[i][r] = True

            l += 1
            r -= 1

        total += l_total + r_total

    return total

def count_visible(input):
    grid = [[False for _ in range(len(input[0]))] for _ in range(len(input))]

    result = count_visible_tb(input, grid) + count_visible_lr(input, grid)

    return result

def part_one(input):
    return count_visible(input)

def scenic_score(input, x, y):
    if x == 0 or y == 0 or x == len(input[0]) - 1 or y == len(input) - 1:
        return 0

    tree = int(input[y][x])

    # UP
    up_score = 0
    for i in range(y - 1, -1, -1):
        view_tree = int(input[i][x])

        up_score += 1

        if view_tree >= tree:
            break

    # DOWN
    down_score = 0
    for i in range(y + 1, len(input)):
        view_tree = int(input[i][x])

        down_score += 1
        
        if view_tree >= tree:
            break

    # LEFT
    left_score = 0
    for j in range(x - 1, -1, -1):
        view_tree = int(input[y][j])

        left_score += 1

        if view_tree >= tree:
            break

    # RIGHT
    right_score = 0
    for j in range(x + 1, len(input[0])):
        view_tree = int(input[y][j])

        right_score += 1

        if view_tree >= tree:
            break

    return up_score * down_score * left_score * right_score
    

def highest_scenic_score(input):
    result = 0

    scores = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    for i in range(len(input)):
        for j in range(len(input[i])):
            ss = scenic_score(input, j, i)

            scores[i][j] = ss

            result = max(result, ss)

    return result

def part_two(input):
    return highest_scenic_score(input)

###
#
# System code below
#
###

def use_test():
    args = set(sys.argv[1:])

    return '--test' in args or '-t' in args

def read_input():
    file_name = 'input.txt'

    if use_test():
        print('Using test input...')
        file_name = 'test.txt'

    with open(f'{sys.path[0]}/{file_name}') as file:
        return file.read().splitlines()

def timeout_handler(signum, frame):
    raise TimeoutError()

def run_part(name, function, input):
    signal.signal(signal.SIGALRM, timeout_handler)

    signal.alarm(10)

    try:
        output = function(input)
        print(f'{name}: {output}')
    except TimeoutError:
        print(f'{name}: TIMEOUT')

    signal.alarm(0)

def main():
    input = read_input()

    run_part('Part 1', part_one, input)
    run_part('Part 2', part_two, input)

if __name__ == '__main__':
    main()
