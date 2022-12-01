import sys

input = []

with open(f'{sys.path[0]}/input.txt') as file:
    input = file.read().splitlines()


def result(opponent, you):
    if (opponent == 'A' and you == 'X') or (opponent == 'B' and you == 'Y') or (opponent == 'C' and you == 'Z'):
        return 3

    if (opponent == 'A' and you == 'Y') or (opponent == 'B' and you == 'Z') or (opponent == 'C' and you == 'X'):
        return 6

    return 0


def score(opponent, you):
    values = {'X': 1, 'Y': 2, 'Z': 3}

    return values[you] + result(opponent, you)


def main():
    total = 0

    for line in input:
        opponent, you = line.split(' ')
        total += score(opponent, you)

    print(total)


if __name__ == '__main__':
    main()
