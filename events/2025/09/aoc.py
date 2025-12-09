from shapely import Polygon

def area(p1, p2):
    return (abs(p1[1] - p2[1]) + 1) * (abs(p1[0] - p2[0]) + 1)

def parse_tiles(input: list[str]) -> list[tuple[int]]:
    return [tuple([int(n) for n in line.split(",")]) for line in input]
    
def parse_edges(tiles: list[tuple[int]]) -> list[tuple[tuple[int]]]:
    segments = []
    for i in range(len(tiles)):
        segments.append((tiles[i], tiles[(i + 1) % len(tiles)]))
    return segments

def rect_polygon(p1, p2):
    c1 = (p1[0], p2[1])
    c2 = (p2[0], p1[1])

    return Polygon([p1, c1, p2, c2, p1])

def part_one(input: list[str]):
    tiles = parse_tiles(input)

    result = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            result = max(result, area(tiles[i], tiles[j]))

    return result

def part_two(input: list[str]):
    tiles = parse_tiles(input)

    polygon = Polygon(tiles + [tiles[0]])

    rects = {}
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            p1 = tiles[i]
            p2 = tiles[j]

            rect = rect_polygon(p1, p2)
            rects[(p1, p2)] = rect

    result = 0
    for pair in rects.keys():
        rect = rects[pair]
        if polygon.contains(rect):
            # Use the original pair to calculate rectangle area, because Polygon's sides are off by one
            result = max(result, area(pair[0], pair[1]))

    return result
