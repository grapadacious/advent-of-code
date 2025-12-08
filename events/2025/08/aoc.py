import math

def euclidian_distance(point_1, point_2):
    p1 = (point_1[0] - point_2[0]) ** 2
    p2 = (point_1[1] - point_2[1]) ** 2
    p3 = (point_1[2] - point_2[2]) ** 2

    return math.sqrt(p1 + p2 + p3)

def parse_point(point: str) -> tuple[int]:
    return tuple(int(n) for n in point.split(","))

def closest_connections(points: list[tuple[int]]):
    connections = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point_1 = points[i]
            point_2 = points[j]
            connections.append([euclidian_distance(point_1, point_2), point_1, point_2])

    connections.sort(key=lambda connection: connection[0])

    return connections

def add_connection(circuits: list[set[tuple[int]]], connection: set[tuple[int]]):
    found_i = 0

    for i in range(len(circuits)):
        circuit_1 = circuits[i]

        if not circuit_1.isdisjoint(connection):
            connection = connection.difference(circuit_1)
            circuits[i] = circuit_1.union(connection)
            found_i = i
            break

    if len(connection) == 0:
        return circuits

    # Merge circuits of both junction boxes because they were in different circuits
    for i in range(found_i + 1, len(circuits)):
        if not circuits[i].isdisjoint(connection):
            circuits[found_i] = circuits[found_i].union(circuits[i])
            found_i = i
            break

    circuits.remove(circuits[found_i])

    return circuits


def part_one(input: list[str]):
    points = [parse_point(point) for point in input]
    circuits = [set([point]) for point in points]
    connections = closest_connections(points)

    # This number is 10 in the example, but is 1000 for the actual problem
    for connection in connections[:1000]:
        circuits = add_connection(circuits, set([connection[1], connection[2]]))

    circuits.sort(reverse=True, key=lambda circuit: len(circuit))

    result = 1

    for circuit in circuits[:3]:
        result *= len(circuit)

    return result

def part_two(input: list[str]):
    points = [parse_point(point) for point in input]
    circuits = [set([point]) for point in points]
    connections = closest_connections(points)

    for connection in connections:
        circuits = add_connection(circuits, set([connection[1], connection[2]]))

        if len(circuits) == 1:
            return connection[1][0] * connection[2][0]
        
    return 0
