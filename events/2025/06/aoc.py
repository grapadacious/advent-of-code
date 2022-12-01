def perform_operation(group: list[str], operation: str):
    group = [int(n) for n in group]

    if operation == "+":
        return sum(group)
    
    total = 1

    for n in group:
        total *= n

    return total

def parse_groups(input: list[str]):
    operations = []

    sub = ""
    for c in input[len(input) - 1]:
        if (c == "+" or c == "*") and sub != "":
            operations.append(sub[:len(sub) - 1])
            sub = ""

        sub += c

    operations.append(sub)
    groups = [[] for _ in operations]

    for i in range(len(input) - 1):
        li = 0
        line = input[i]
        for oi in range(len(operations)):
            operation = operations[oi]
            lo = len(operation)
            groups[oi].append(line[li:li + lo])
            li += lo + 1

    return (groups, [o.strip() for o in operations])

def part_one(input: list[str]):
    groups, operations = parse_groups(input)
    total = 0

    for i in range(len(groups)):
        total += perform_operation(groups[i], operations[i])

    return total

def map_group_to_ceph(group: list[int]) -> list[int]:
    max_places = max([len(str(n)) for n in group])
    result = ["" for _ in range(max_places)]

    for i in range(len(result)):
        for n in group:
            result[i] += n[i]

    return [int(n) for n in result]

def part_two(input: list[str]):
    groups, operations = parse_groups(input)
    total = 0

    for i in range(len(groups)):
        group = map_group_to_ceph(groups[i])
        total += perform_operation(group, operations[i])

    return total
