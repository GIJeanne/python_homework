#Task 5: Extending a Class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def euclidean_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    # Uses Point.__init__ unchanged.

    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    # Point
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    p3 = Point(1, 2)
    print("p1:", p1)
    print("p2:", p2)
    print("p1 == p3:", p1 == p3)
    print("p1 == p2:", p1 == p2)
    print("distance p1 to p2:", p1.euclidean_distance(p2))

    # Vector
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector(1, 2)
    print("v1:", v1)
    print("v2:", v2)
    print("v1 == v3:", v1 == v3)
    print("v1 == v2:", v1 == v2)
    print("distance v1 to v2:", v1.euclidean_distance(v2))
    v4 = v1 + v2
    print("v1 + v2:", v4)
    print("v1 + v2 is a Vector:", isinstance(v4, Vector))