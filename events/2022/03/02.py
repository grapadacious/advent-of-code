import sys

input = []

with open(f'{sys.path[0]}/input.txt') as file:
    input = file.read().splitlines()

priority = {}

for i in range(1, 27):
    priority[chr(i + 96)] = i
    priority[chr(i + 64)] = i + 26


def find_badge(group):
    first_rucksack = set(group[0])
    second_sucksack = set(group[1])

    for item in group[2]:
        if item in first_rucksack and item in second_sucksack:
            return item


def main():
    total = 0

    for i in range(0, len(input), 3):
        group = input[i:i + 3]
        badge = find_badge(group)
        total += priority[badge]

    print(total)


if __name__ == '__main__':
    main()
