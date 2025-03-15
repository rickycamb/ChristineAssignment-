class Shape:
    def __init__(self):
        # Initialization logic for Shape
        print("Initializing Shape")

    def calculate_area(self):
        # This method can be overridden in derived classes
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        # Call the constructor of the Shape class
        super().__init__()
        self.width = width
        self.height = height
        print("Initializing Rectangle")

    def calculate_area(self):
        # Calculate the area of the rectangle
        return self.width * self.height

# Example usage:
rectangle = Rectangle(4, 5)
area = rectangle.calculate_area()

print(f"Area of the rectangle: {area}")
