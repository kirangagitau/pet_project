#!/usr/bin/python3
'''use the python 3 interpreter'''

import random


def macx_gui():
    x = input("How many scores?  {:d}".format(x))
    students = abs(x)
    while students != 0:
        x = random.randint(28, 63)
        print("{:d} ".format(x))
        students -= 1  # decrement counts
    return


macx_gui()  # calling the function

''' The above program generates some random
score values for a given number of students in
a given range and prints them in a given file
It does not append'''
