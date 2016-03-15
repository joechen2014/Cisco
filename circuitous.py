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
        'Most people do not read docstrings on magic methods'
        self.radius = radius
        
    def __repr__(self):
        return ('%s(radius=%r)' % (self.__class__.__name__, self.radius))

    def area(self):
        'Perform quadrature on a planar of uniform revolution'
        return math.pi * self.radius ** 2

    def perimeter(self):
        'Something really smart sounding...'
        return math.pi * self.radius * 2

    'turn off self'
    @staticmethod
    def angle_to_grade(angle):
        '''
        Returns a percent grade given an
        inclinometer reading in degrees

            >>> Circle.angle_to_grade(7)
            12.27845609029046
        '''
        return math.tan(math.radians(angle)) * 100

if __name__ == "__main__":
    c = Circle(5)
    print c
    
