from graphics import *


class Platforms:

    def __init__(self, x, x2, y, y2):
        self.x = x
        self.x2 = x2
        self.y = y
        self.y2 = y2
        self.rect = Rectangle(Point(x, y), Point(x2, y2))
        self.rect.setOutline("white")

    def show(self, window):
        """Shows platforms"""
        self.rect.undraw()


class Slime:

    def __init__(self, x, y, r):
        """Animation lists"""
        self.x = x      # Center of the slime
        self.y = y
        self.r = r       # Radius of the slime, unless a different hitbox
        self.circle = Circle(Point(x, y), r)
        self.circle.setOutline("white")
        self.run = []
        self.jump = []
        self.death = []

    def show(self, window):
        """Shows the collision box"""
        self.circle.undraw()

