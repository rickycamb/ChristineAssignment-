import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area

# Example usage:
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3)
]

total_area = calculate_total_area(shapes)
print(f"Total area of all shapes: {total_area:.2f}")
