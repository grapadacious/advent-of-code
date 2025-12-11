import math

def between(a, b, c, inclusive=False):
    if inclusive:
        return min(a, b) <= c and max(a, b) >= c
    
    return min(a, b) < c and max(a, b) > c

def perpendicular(a: tuple[tuple[int]], b: tuple[tuple[int]]) -> bool:
    if a[0][0] == a[1][0] and b[0][1] == b[1][1]:
            return True
        
    if a[0][1] == a[1][1] and b[0][0] == b[1][0]:
        return True
    
    return False

def intersect(a: tuple[tuple[int]], b: tuple[tuple[int]]) -> bool:
    if not perpendicular(a, b):
        return False
    
    if a[0] == b[0] or a[1] == b[0] or a[0] == b[1] or a[1] == b[1]:
        return False
    
    # a is vertical
    if a[0][0] == a[1][0]:
        return between(a[0][1], a[1][1], b[0][1], True) and between(b[0][0], b[1][0], a[0][0], True)
    # a is horizontal
    else:
        return between(b[0][1], b[1][1], a[0][1], True) and between(a[0][0], a[1][0], b[0][0], True)

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def points(self):
        i = 0

        if self.a.x == self.b.x:
            i = 1

        edge = ((self.a.x, self.a.y), (self.b.x, self.b.y))
        min_i = min([edge[0][i], edge[1][i]])
        max_i = max([edge[0][i], edge[1][i]])

        for vi in range(min_i + 1, max_i):
            p = [self.a.x, self.a.y]
            p[i] = vi
            yield Point(p[0], p[1])

    def contains(self, point: Point) -> bool:
        if self.a.x == self.b.x:
            return point.x == self.a.x and self._between(self.a.y, self.b.y, point.y, True)
        
        return point.y == self.a.y and self._between(self.a.x, self.b.x, point.x, True)

    def intersects(self, other: "Line") -> bool:
        if not self._perpendicular(other):
            return False
        
        if self.a == other.a or self.b == other.a or self.a == other.b or self.b == other.b:
            return False
        
        # if self.contains(other.a) or self.contains(other.b) or other.contains(self.a) or other.contains(self.b):
        #     return True
        
        # TODO: Fix/implement intersection logic
        # self is vertical
        if self.a.x == self.b.x:
            return self._between(self.a.y, self.b.y, other.a.y, True) and self._between(other.a.x, other.b.x, self.a.x, True)
        # self is horizontal
        else:
            return self._between(other.a.y, other.b.y, self.a.y, True) and self._between(self.a.x, self.b.x, other.a.x, True)

    def _perpendicular(self, other: "Line") -> bool:
        if self.a.x == self.b.x and other.a.y == other.a.y:
            return True
        
        if self.a.y == self.b.y and other.a.x == other.b.x:
            return True
        
        return False

    def _between(self, a, b, c, inclusive=False):
        if inclusive:
            return min(a, b) <= c and max(a, b) >= c
        
        return min(a, b) < c and max(a, b) > c
    
    def length(self):
        if self.a.x == self.b.x:
            return int(abs(self.a.y - self.b.y)) + 1
        else:
            return int(abs(self.a.x - self.b.x)) + 1
    
    def __repr__(self):
        return f"{self.a} -> {self.b}: {self.length()}"
    
class Rect:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        return self.sides[0].length() * self.sides[1].length()
    
    @classmethod
    def from_corners(cls, p1, p2):
        p3 = Point(p1.x, p2.y)
        p4 = Point(p2.x, p1.y)

        return cls([Line(p1, p3), Line(p3, p2), Line(p2, p4), Line(p4, p1)])
    
    def __repr__(self):
        return f"{', '.join([str(side.a) for side in self.sides])}: {self.area()}"
