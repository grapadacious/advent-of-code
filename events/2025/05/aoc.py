def is_fresh(ingredient, fresh_range):
    ingredient = int(ingredient)
    low, high = [int(n) for n in fresh_range.split("-")]

    if ingredient >= low and ingredient <= high:
        return True
    
    return False

def overlaps(range_1, range_2):
    if range_2[0] <= range_1[1]:
        return True
    
    return False

def merge_ranges(range_1, range_2):
    return [range_1[0], max(range_1[1], range_2[1])]

def reduce_ranges(ranges):
    current_range = ranges[0]
    reduced_ranges = []

    for i in range(1, len(ranges)):

        if not overlaps(current_range, ranges[i]):
            reduced_ranges.append(current_range)
            current_range = ranges[i]
            continue

        current_range = merge_ranges(current_range, ranges[i])

    reduced_ranges.append(current_range)

    return reduced_ranges

def part_one(input: list[str]):
    fresh_ranges = []
    start_ids = 0
    total = 0

    for i in range(len(input)):
        line = input[i]

        if line == "":
            start_ids = i + 1
            break

        fresh_ranges.append(line)

    for i in range(start_ids, len(input)):
        for fresh_range in fresh_ranges:
            if is_fresh(input[i], fresh_range):
                total += 1
                break

    return total

def part_two(input: list[str]):
    ranges = []

    for i in range(len(input)):
        line = input[i]

        if line == "":
            break

        ranges.append([int(i) for i in line.split("-")])

    ranges = sorted(ranges, key=lambda x: x[0])
    reduced_ranges = reduce_ranges(ranges)

    total = 0

    for r in reduced_ranges:
        total += (r[1] - r[0]) + 1

    return total
