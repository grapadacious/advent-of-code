def find_max_joltage(bank, n_selections=2):
    positions = [0 for _ in range(n_selections)]

    prev_pos = -1

    for pos_i in range(len(positions)):
        positions[pos_i] = prev_pos + 1
        end = len(bank) - (len(positions) - pos_i - 1)

        for i in range(prev_pos + 1, end):
            if int(bank[i]) > int(bank[positions[pos_i]]):
                positions[pos_i] = i

        prev_pos = positions[pos_i]

    return int("".join([bank[pos] for pos in positions]))


def part_one(input: list[str]):
    total = 0
    for line in input:
        total += find_max_joltage(line)
    return total


def part_two(input: list[str]):
    total = 0
    for line in input:
        total += find_max_joltage(line, 12)
    return total
