import sys

input = []

with open(f'{sys.path[0]}/input.txt') as file:
    input = file.read().splitlines()


def size(range):
    return range[1] - range[0]


def prepare(line):
    result = []

    for r in line.split(','):
        result.append(list(map(int, r.split('-'))))

    return result


def is_contained(larger, smaller):
    larger_set = set(range(larger[0], larger[1] + 1))

    for n in range(smaller[0], smaller[1] + 1):
        if n not in larger_set:
            return False

    return True


def is_bad(pair):
    first_size = size(pair[0])
    second_size = size(pair[1])

    larger = pair[0]
    smaller = pair[1]

    if first_size < second_size:
        larger = pair[1]
        smaller = pair[0]

    return is_contained(larger, smaller)


def main():
    total = 0

    for line in input:
        pair = prepare(line)

        if is_bad(pair):
            total += 1

    print(total)


if __name__ == '__main__':
    main()
