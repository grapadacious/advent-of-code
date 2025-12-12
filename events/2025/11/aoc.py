from functools import cache

graph = {}

def build_graph(input: list[str]):
    for line in input:
        segments = line.split(" ")
        graph[segments[0][:-1]] = set(segments[1:])

@cache
def count_paths_recursive(device: str, visited_dac=True, visited_fft=True):
    if device == "out":
        return 1 if visited_dac and visited_fft else 0

    if device == "dac":
        visited_dac = True

    if device == "fft":
        visited_fft = True

    result = 0
    for next in graph[device]:
        result += count_paths_recursive(next, visited_dac, visited_fft)

    return result

def part_one(input: list[str]):
    build_graph(input)

    return count_paths_recursive("you")

def part_two(input: list[str]):
    build_graph(input)

    return count_paths_recursive("svr", False, False)
