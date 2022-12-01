def count_adjacent(grid: list[str], r: int, c: int):
    total = 0

    for ir in range(r - 1, r + 2):
        for ic in range(c - 1, c + 2):
            if ir < 0 or ir >= len(grid) or ic < 0 or ic >= len(grid[ir]):
                continue

            if ir == r and ic == c:
                continue

            if grid[ir][ic] == "@":
                total += 1

    return total

def count_removable_rolls(input: list[str], remove=False):
    total = 0

    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] != "@":
                continue

            if count_adjacent(input, r, c) < 4:
                if remove:
                    input[r][c] = "X"
                total += 1

    return total

def part_one(input: list[str]):
    return count_removable_rolls(input)

def part_two(input: list[list[str]]):
    total = 0

    while True:
        removed = count_removable_rolls(input, True)

        total += removed

        if removed == 0:
            break

    return total
