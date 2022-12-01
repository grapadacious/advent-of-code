import sys

def use_test():
    args = set(sys.argv[1:])

    return '--test' in args or '-t' in args

def read_input():
    file_name = 'input.txt'

    if use_test():
        print('Using test input...')
        file_name = 'test.txt'

    with open(f'{sys.path[0]}/{file_name}') as file:
        return file.read().splitlines()[0]

def find_first_unique(input, length):
    result = len(input) + 1
    for i in range(len(input), length, -1):
        marker = set(input[i - length:i])

        if len(marker) == length:
            result = i

    return result

def part_one(input):
    return find_first_unique(input, 4)

def part_two(input):
    return find_first_unique(input, 14)

def main():
    input = read_input()

    part_one_output = part_one(input)
    part_two_output = part_two(input)

    print(f'Part 1: {part_one_output}')
    print(f'Part 2: {part_two_output}')


if __name__ == '__main__':
    main()
