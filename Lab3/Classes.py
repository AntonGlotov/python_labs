import math
import turtle


class Triangle:
    def __init__(self, coord_x=0, coord_y=0, size=100, color="blue"):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.size = size
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.coord_x, self.coord_y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(self.size)
            turtle.left(120)
        turtle.end_fill()

    def move(self, distance_x, distance_y):
        self.coord_x += distance_x
        self.coord_y += distance_y

    def area(self):
        s = (self.size ** 2 * math.sqrt(3)) / 4
        return s


class Rectangle:
    def __init__(self, coord_x=0, coord_y=0, size=100, color="red"):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.size = size
        self.color = color

    def move(self, distance_x, distance_y):
        self.coord_x += distance_x
        self.coord_y += distance_y

    def area(self):
        s = 2 * self.size * self.size
        return s

    def draw(self):
        turtle.penup()
        turtle.goto(self.coord_x, self.coord_y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(1, 5):
            turtle.forward(self.size + self.size * (i % 2))
            turtle.left(90)
        turtle.end_fill()


rect = Rectangle(color="brown")
rect.draw()
rect.move(0, 100)
rect.draw()
tri = Triangle(0, 200, 200)
tri.draw()
rect.color = "white"
rect.size = 50
rect.move(50, -75)
rect.draw()
rect.move(0, 100)
rect.draw()
turtle.done()
