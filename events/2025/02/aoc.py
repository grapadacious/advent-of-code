import re

def shared(input: list[str], regex: str):
    total = 0

    for r in input:
        low, high = r.split('-')

        for i in range(int(low), int(high) + 1):
            if re.match(regex, str(i)) is not None:
                total += i

    return total

def part_one(input: list[str]):
    return shared(input, r"^(.*)\1$")

def part_two(input: list[str]):
    return shared(input, r"^(.*)\1+$")
