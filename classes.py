from graphics import *


class Platforms:

    def __init__(self, x, x2, y, y2):
        self.x = x
        self.x2 = x2
        self.y = y
        self.y2 = y2


class Slime:

    def __init__(self, x, r):
        """Animation lists"""
        self.x = x
        self.r = r
        self.run = []
        self.jump = []
        self.death = []
