from .geometry import Line, Point, Rect

def parse_tile_points(input: list[str]) -> list[Point]:
    result = []
    for line in input:
        x, y = [float(n) for n in line.split(",")]
        result.append(Point(x, y))
    return result
    
def parse_edges(tiles: list[tuple[int]]) -> list[tuple[tuple[int]]]:
    segments = []
    for i in range(len(tiles)):
        segments.append((tiles[i], tiles[(i + 1) % len(tiles)]))
    return segments

def rect_lines(p1, p2):
    p3 = Point(p1.x, p2.y)
    p4 = Point(p2.x, p1.y)

    return [Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)]

def part_one(input: list[str]):
    tiles = parse_tile_points(input)

    result = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            rect = Rect.from_corners(tiles[i], tiles[j])
            result = max(result, rect.area())

    return result

def part_two(input: list[str]):
    tiles = parse_tile_points(input)

    polygon_sides = []
    for i in range(len(tiles)):
        p1 = tiles[i]
        p2 = tiles[(i + 1) % len(tiles)]

        polygon_sides.append(Line(p1, p2))

    rects = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            rects.append(Rect.from_corners(tiles[i], tiles[j]))

    result = 0
    for rect in rects:
        intersects = False
        for polygon_side in polygon_sides:
            for rect_side in rect.sides:
                intersects = intersects or polygon_side.intersects(rect_side)

        if not intersects:
            result = max(result, rect.area())

    return result
