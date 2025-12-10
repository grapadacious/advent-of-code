import math

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def intersects(self, other: "Line") -> bool:
        if not self._perpendicular(other):
            return False
        
        # TODO: Fix/implement intersection logic
        # self is vertical
        if self.a.x == self.b.x:
            pass
        # self is horizontal
        else:
            pass
        
        return False

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
