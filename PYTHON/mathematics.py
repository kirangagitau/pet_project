#!/usr/bin/python3

import math  # maths in general.
import statistics as st # import module for stats as st
import random  # tool for random selection.


''' this function makes use of the math module'''
def mathematics():
    print(math.cos(math.pi / 4))
    print(math.log(1024, 2))
    return;


''' this function makes use of the random module'''
def random_module():
    choice = random.choice(['apple', 'pear', 'banan'])  # choose any
    x = random.random()  # random float
    y = random.randrange(20)  # random int from range 20
    
    print('\n')
    print(choice)
    print(x)
    print(y)
    return;


''' This func uses the statistics module'''
def statisticals():
    scores = [20, 50, 10, 30, 40, 70, 100, 80, 90, 60]
    mx = st.mean(scores)
    md = st.median(scores)
    var = st.variance(scores) 
    maximum = max(scores)
    minimum = min(scores)
    rn = maximum - minimum

    print('Score mean is: ', mx)
    print('Score Median is: ', md)
    print('Score variance is: ',var)
    print("the Range is: ")
    print(rn)
    return;

'''
Now after defining all the functions it is now time to call each 
and every function to perform its specified actions. In this case since no parameters 
were specified for the said functions, the functions are thus called without any arguments
being passed to them. The order in which they are called is what determines the order of 
execution rather than the order of their declaration.
'''

statisticals()
mathematics()
random_module()
