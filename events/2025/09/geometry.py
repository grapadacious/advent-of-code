import math

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
        generator = self.vertical_points if self.a.x == self.b.x else self.horizontal_points

        for point in generator():
            yield point

    def contains(self, point: Point) -> bool:
        if self.a.x == self.b.x:
            if point.x != self.a.x:
                return False
            else:
                min_y = min(self.a.y, self.b.y)
                max_y = max(self.a.y, self.b.y)
                return point.y >= min_y and point.y <= max_y
        else:
            if point.y != self.a.y:
                return False
            else:
                min_x = min(self.a.x, self.b.x)
                max_x = max(self.a.x, self.b.x)
                return point.x >= min_x and point.x <= max_x

    def vertical_points(self):
        y = min(self.a.y, self.b.y)
        max_y = max(self.a.y, self.b.y)

        while y <= max_y:
            yield Point(self.a.x, y)
            y += 1

    def horizontal_points(self):
        x = min(self.a.x, self.b.x)
        max_x = max(self.a.x, self.b.x)

        while x <= max_x:
            yield Point(x, self.a.y)
            x += 1

    def intersects(self, other: "Line") -> bool:
        if not self._perpendicular(other):
            return False
        
        if self.a == other.a or self.b == other.a or self.a == other.b or self.b == other.b:
            return False
        
        if self.contains(other.a) or self.contains(other.b) or other.contains(self.a) or other.contains(self.b):
            return True
        
        # TODO: Fix/implement intersection logic
        # self is vertical
        if self.a.x == self.b.x:
            min_y = min(self.a.y, self.b.y)
            max_y = max(self.a.y, self.b.y)
            min_x = min(other.a.x, other.b.x)
            max_x = max(other.a.x, other.b.x)

            return other.a.y > min_y and other.a.y < max_y and self.a.x > min_x and self.a.x < max_x
        # self is horizontal
        else:
            min_y = min(other.a.y, other.b.y)
            max_y = max(other.a.y, other.b.y)
            min_x = min(self.a.x, self.b.x)
            max_x = max(self.a.x, self.b.x)

            return other.a.x > min_x and other.a.x < max_x and self.a.y > min_y and self.a.y < max_y

    def _perpendicular(self, other: "Line") -> bool:
        if self.a.x == self.b.x and other.a.y == other.a.y:
            return True
        
        if self.a.y == self.b.y and other.a.x == other.b.x:
            return True
        
        return False

    def _between(self, a, b, c):
        return min(a, b) < c and max(a, b) > c
    
    def length(self):
        result = int(abs(self.a.x - self.b.x))

        if self.a.x == self.b.x:
            result = int(abs(self.a.y - self.b.y))

        return result + 1
    
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
