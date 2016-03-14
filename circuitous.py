'''
    Copyright (c) 2016 Ciruitous(tm)
    All rights reserved.

Eric Ries, "Lean Startup Method"
YAGNI - Ya ain't gonna need it

Agile : Waterfall :: Lean Startup : Business Plan
'''
import math

class Circle:
    '''
    An advanced circle analytics toolkit
    '''

    def __init__(self, radius):
        self.radius = radius
    def __repr__(self):
        return ('Circle(radius=%r)' % self.radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * self.radius * 2

if __name__ == "__main__":
    c = Circle(5)
