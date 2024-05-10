#!/usr/bin/python3

''' a function to illustrate while
loops in python
'''


def while_loop():
    count = 0
    while (count <= 20):
        print('Number position: {}'.format(count))
        count += 1
    return


while_loop()  # calling the function
