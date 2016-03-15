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

class Circle(object):
    '''
    An advanced circle analytics toolkit
    '''

    version = Version(0, 8)
    
    def __init__(self, radius):
        'Most people do not read docstrings on magic methods'
        self.radius = radius

    @classmethod
    def from_bbd(cls, diagonal):
        'Build a Circle from a bounding box diagonal'
        radius = diagonal / math.sqrt(2)
        return cls(radius)

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, value):
        self.diameter = value * 2.0
        
    def __repr__(self):
        return ('%s(radius=%r)' % (self.__class__.__name__, self.radius))

    def area(self):
        'Perform quadrature on a planar of uniform revolution'
        radius = self.__perimeter() / math.pi / 2.0
        return math.pi * radius ** 2

    def perimeter(self):
        'Something really smart sounding...'
        return math.pi * self.radius * 2

    __perimeter = perimeter

    'turn off self'
    @staticmethod
    def angle_to_grade(angle):
        '''
        Returns a percent grade given an
        inclinometer reading in degrees

            >>> print Circle.angle_to_grade(7)
            12.2784560903
        '''
        return math.tan(math.radians(angle)) * 100

if __name__ == "__main__":
    c = Circle(5)
    print c
    
