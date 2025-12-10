from .geometry import Line, Point, Rect
from .grid import Grid

def parse_tile_points(input: list[str]) -> list[Point]:
    result = []
    for line in input:
        x, y = [int(n) for n in line.split(",")]
        result.append(Point(x, y))
    return result

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

    max_x = max(t.x for t in tiles)
    max_y = max(t.y for t in tiles)

    grid = Grid(max_x + 3, max_y + 2)
    
    polygon_sides = []
    for i in range(len(tiles)):
        p1 = tiles[i]
        p2 = tiles[(i + 1) % len(tiles)]

        polygon_sides.append(Line(p1, p2))

    rects = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            rects.append(Rect.from_corners(tiles[i], tiles[j]))

    # grid.draw_points(tiles, "#")
    # grid.draw_lines(polygon_sides, "X")
    # grid.print()

    result = 0
    for rect in rects:
        intersects = False
        for polygon_side in polygon_sides:
            for rect_side in rect.sides:
                intersects = polygon_side.intersects(rect_side)

                if intersects:
                    break

            if intersects:
                break

        if not intersects:
            result = max(result, rect.area())

    return result
