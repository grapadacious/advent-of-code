def print_polygon(tiles, polygon_edges=[], rect_edges=[]):
    min_x = min([t[0] for t in tiles])
    max_x = max([t[0] for t in tiles])
    min_y = min([t[1] for t in tiles])
    max_y = max([t[1] for t in tiles])

    grid = [["." for x in range(max_x + min_x + 1)] for y in range(max_y + min_y + 1)]

    for t in tiles:
        grid[t[1]][t[0]] = "#"

    for edge in polygon_edges:
        i = 0

        if edge[0][0] == edge[1][0]:
            i = 1

        min_i = min([edge[0][i], edge[1][i]])
        max_i = max([edge[0][i], edge[1][i]])

        for vi in range(min_i + 1, max_i):
            p = list(edge[0])
            p[i] = vi
            if grid[p[1]][p[0]] == ".":
                grid[p[1]][p[0]] = "X"

    for edge in rect_edges:
        i = 0

        if edge[0][0] == edge[1][0]:
            i = 1

        min_i = min([edge[0][i], edge[1][i]])
        max_i = max([edge[0][i], edge[1][i]])

        for vi in range(min_i, max_i + 1):
            p = list(edge[0])
            p[i] = vi
            grid[p[1]][p[0]] = "0"

    for row in grid:
        print("".join(row))

    print()