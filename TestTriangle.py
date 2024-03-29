# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

#from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework



class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
 
    def testInvalidInput(self):
        self.assertEqual(classify_triangle(-1,3, 4), 'InvalidInput')

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene', '2, 3, 4 should be scalene')

    def testIsocelesTriangle(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isoceles', '2, 2, 3 should be isoceles')

    def testTriangleInequality(self):
        self.assertEqual(classify_triangle(1, 2, 4), 'NotATriangle', '1, 2, 4 should not be a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

