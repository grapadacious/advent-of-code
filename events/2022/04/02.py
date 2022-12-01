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


def in_range(n, r):
    return n >= r[0] and n <= r[1]


def overlap(pair):
    first = pair[0]
    second = pair[1]

    return in_range(first[0], second) or in_range(first[1], second) or in_range(second[0], first) or in_range(second[1], first)


def main():
    total = 0

    for line in input:
        pair = prepare(line)

        if overlap(pair):
            total += 1

    print(total)


if __name__ == '__main__':
    main()
