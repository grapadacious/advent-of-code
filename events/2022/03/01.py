import sys

input = []

with open(f'{sys.path[0]}/input.txt') as file:
    input = file.read().splitlines()

priority = {}

for i in range(1, 27):
    priority[chr(i + 96)] = i
    priority[chr(i + 64)] = i + 26


def find_item(rucksack):
    midpoint = len(rucksack) // 2

    lookup = set(rucksack[:midpoint])

    for item in rucksack[midpoint:]:
        if item in lookup:
            return item


def main():
    total = 0

    for line in input:
        item = find_item(line)
        total += priority[item]

    print(total)


if __name__ == '__main__':
    main()
