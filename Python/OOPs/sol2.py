"""
Q2. write a python program to create a class circle with a attribute radius and 
two methods to find the area and circumference of the circle.

"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Attribute for the radius of the circle

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":

    my_circle = Circle(5)

    print(f"Area of the circle: {my_circle.area():.2f}")
    print(f"Circumference of the circle: {my_circle.circumference():.2f}")

