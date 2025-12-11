from .geometry import Line, Point, Rect, intersect
from .grid import Grid

def area(c1, c2):
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)

def parse_tile_points(input: list[str]) -> list[Point]:
    result = []
    for line in input:
        x, y = [int(n) for n in line.split(",")]
        result.append(Point(x, y))
    return result

def parse_tile_tuples(input: list[str]) -> list[tuple[int]]:
    result = []
    for line in input:
        result.append(tuple(int(n) for n in line.split(",")))
    return result

def part_one(input: list[str]):
    tiles = parse_tile_tuples(input)

    result = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            result = max(result, area(tiles[i], tiles[j]))

    return result

def part_two(input: list[str]):
    tiles = parse_tile_tuples(input)
    
    polygon_sides = []
    for i in range(len(tiles)):
        p1 = tiles[i]
        p2 = tiles[(i + 1) % len(tiles)]

        polygon_sides.append((p1, p2))

    rects = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            p1 = tiles[i]
            p3 = tiles[j]
            p2 = (p1[0], p3[1])
            p4 = (p3[0], p1[1])

            rects.append([(p1, p2), (p2, p3), (p3, p4), (p4, p1)])

    result = 0
    for rect in rects:
        intersects = False
        for rect_side in rect:
            for polygon_side in polygon_sides:
                intersects = intersect(polygon_side, rect_side)

                if intersects:
                    break

            if intersects:
                break

        if not intersects:
            result = max(result, area(rect[0][0], rect[1][1]))

    return result
