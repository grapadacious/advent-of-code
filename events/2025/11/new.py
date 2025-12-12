import gc

def build_graph(input: list[str]):
    result = {}

    for line in input:
        segments = line.split(" ")
        result[segments[0][:-1]] = set(segments[1:])

    return result

def count_paths_recursive(start: str, graph: dict[str, set[str]], possible: str[str], path=set(), end: str="out", required=set(["dac, fft"])):
    total = 0

    if end in graph[start]:
        return 1 if required.issubset(path) else 0

    for next in graph[start]:
        if next not in possible:
            continue

        if next in path:
            continue

        path.add(next)

        total += count_paths_recursive(next, graph, possible, path, end, required)

        path.remove(next)

    return total

def count_paths_recursive(device: str, graph: dict[str, set[str]], possible: set[str], path: set[str]=set(), end: str="out", required=set()):
    if device == end:
        return 1
    
    if device in path:
        return 0
    
    path.add(device)

    result = 0
    for next in graph[device]:
        result += count_paths_recursive(next, graph, possible, path, end, required)

    path.remove(device)

    return result

def count_paths_iter(start: str, graph: dict[str, list[str]], end: str="out", term: set[str]=set(["out"])):
    queue = [[start, set()]]

    total = 0
    while len(queue) > 0:
        node, path = queue[0]
        queue = queue[1:]

        if end in graph[node]:
            total += 1
            continue

        for destination in graph[node]:
            if destination in term:
                continue

            if destination in path:
                continue

            path = path.union([destination])

            queue.append([destination, path])

    return total

def find_valid_nodes(graph: dict[str, set[str]]):
    queue = ["out"]
    visited = set()

    while len(queue) > 0:
        search = queue[0]
        queue = queue[1:]

        if search == "svr":
            break

        for key, value_set in graph.items():
            if key in visited:
                continue

            if search in value_set:
                visited.add(key)
                queue.append(key)

    return visited

def part_one(input: list[str]):
    graph = build_graph(input)

    return count_paths_iter("you", graph)

def part_two(input: list[str]):
    graph = build_graph(input)
    possible = find_valid_nodes(graph)

    return count_paths_recursive("svr", graph, possible, required=set(["dac", "fft"]))
