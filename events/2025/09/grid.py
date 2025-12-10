from .geometry import Line, Point

class Grid:
    def __init__(self, width, height):
        self._grid = [["." for _ in range(width)] for _ in range(height)]

    def draw_point(self, point: Point, c: str, force=False):
        if force or self._grid[point.y][point.x] == ".":
            self._grid[point.y][point.x] = c

    def draw_points(self, points: list[Point], c: str, force=False):
        for point in points:
            self.draw_point(point, c, force)

    def draw_line(self, line: Line, c: str, force=False):
        for point in line.points():
            self.draw_point(point, c, force)

    def draw_lines(self, lines: list[Line], c: str, force=False):
        for line in lines:
            self.draw_line(line, c, force)

    def clear(self):
        for r in range(len(self._grid)):
            for c in range(len(self._grid[r])):
                self._grid[r][c] = "."

    def print(self):
        print(self)

    def __repr__(self):
        return "\n".join(["".join(row) for row in self._grid])
