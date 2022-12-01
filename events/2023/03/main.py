import signal
import sys

def is_symbol(i, j, input):
    if i < 0 or j < 0 or i > len(input) - 1 or j > len(input[i]) - 1:
        return False
    
    c = input[i][j]

    if c.isdigit():
        return False
    
    if c == '.':
        return False
    
    return True

def check_part(i, j, input):
    result = False

    result = result or is_symbol(i - 1, j - 1, input)
    result = result or is_symbol(i - 1, j, input)
    result = result or is_symbol(i - 1, j + 1, input)
    result = result or is_symbol(i, j - 1, input)
    result = result or is_symbol(i, j + 1, input)
    result = result or is_symbol(i + 1, j - 1, input)
    result = result or is_symbol(i + 1, j, input)
    result = result or is_symbol(i + 1, j + 1, input)

    return result

def find_part_numbers(input):
    result = []

    for i in range(len(input)):
        row = input[i]
        num_s = ''
        is_part = False
        for j in range(len(row)):
            c = row[j]

            if c.isdigit():
                num_s += c
                is_part = is_part or check_part(i, j, input)
                continue

            if len(num_s) > 0 and is_part:
                result.append(int(num_s))

            num_s = ''
            is_part = False

        if len(num_s) > 0 and is_part:
                result.append(int(num_s))
    
    return result

def update_possible_gears(possible_gears, n, star_coords):
    if len(star_coords) < 1:
        return possible_gears
    
    for coords in star_coords:
        if coords not in possible_gears:
            possible_gears[coords] = []

        possible_gears[coords].append(n)

    return possible_gears

def get_stars(i, j, input):
    stars = set()

    for ai in range(i - 1, i + 2):
        for aj in range(j - 1, j + 2):
            if ai == i and aj == j:
                continue
            if ai < 0 or ai > len(input) - 1:
                continue
            if aj < 0 or aj > len(input[ai]) - 1:
                continue
            
            if input[ai][aj] != '*':
                continue

            stars.add((ai, aj))

    return stars

def find_possible_gears(input):
    possible_gears = {}

    for i in range(len(input)):
        row = input[i]
        num_s = ''
        star_coords = set()

        for j in range(len(row)):
            c = row[j]
            
            if c.isdigit():
                num_s += c
                star_coords.update(get_stars(i, j, input))
                continue

            if len(num_s) > 0:
                possible_gears = update_possible_gears(possible_gears, int(num_s), star_coords)

            num_s = ''
            star_coords = set()

        if len(num_s) > 0:
                possible_gears = update_possible_gears(possible_gears, int(num_s), star_coords)

    return possible_gears


def find_gear_ratios(input):
    possible_gears = find_possible_gears(input)
    result = []

    for coords in possible_gears:
        nums = possible_gears[coords]
        if len(nums) == 2:
            result.append(nums[0] * nums[1])

    return result


def part_one(input):
    part_numbers = find_part_numbers(input)

    return sum(part_numbers)

def part_two(input):
    gear_ratios = find_gear_ratios(input)

    return sum(gear_ratios)

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
