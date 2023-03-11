# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(val1,val2,val3):
    """
    Returns the sum of two numbers.
    :param val1: The first number.
    :param val2: The second number.
    :param val3: The third number.
    :return: result
    """
    # require that the input values be >= 0 and <= 200
    if val1 <= 0 or val2 <= 0 or val3 <= 0:
        return 'InvalidInput'
    if val1 > 200 or val2 > 200 or val3 > 200:
        return 'InvalidInput'
    if (val1 >= (val2 + val3))or(val2 >= (val1 + val3))or(val3 >= (val1 + val2)):
        return 'NotATriangle'
    if val1 == val2 and val2 == val3:
        return 'Equilateral'
    if (val1**2+val2**2==val3**2)or(val1**2+val3**2==val2**2)or(val2**2+val3**2==val1**2):
        return 'Right'
    if (val1 != val2) and  (val2 != val3) and (val1 != val3):
        return 'Scalene'
    return 'Isoceles'
    