'''
    Copyright (c) 2016 Ciruitous(tm)
    All rights reserved.

Eric Ries, "Lean Startup Method"
YAGNI - Ya ain't gonna need it

Agile : Waterfall :: Lean Startup : Business Plan
'''
import math
from collections import namedtuple

Version = namedtuple('Version', 'major minor')

class Circle:
    '''
    An advanced circle analytics toolkit
    '''

    version = Version(0, 4)

    def __init__(self, radius):
        self.radius = radius
        
    def __repr__(self):
        return ('%s(radius=%r)' % (self.__class__.__name__, self.radius))

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * self.radius * 2

if __name__ == "__main__":
    c = Circle(5)
    print c
    
