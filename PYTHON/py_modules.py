#!/usr/bin/python3
from calendar import isleap as lp  # import attribute & rename it
import cal  # import user defined module
import math as mt  # import and rename module

'''attributes from the math module'''
print(mt.pi)
print(mt.cos(30))

print(lp(2024))
''' lp as only imported attribute'''

cal.add(9, 8)
'''calling user defined module'''
