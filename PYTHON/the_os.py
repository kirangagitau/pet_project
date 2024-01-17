#!/usr/bin/python3
'''use python 3 to interpret'''

import os  # importing os module
'''the os module is one of the largest module in python
with quite a range of fucntions'''


def workingdr():
    print(os.getcwd())  # func to show working dir
    print("\n")
    print(dir(os))  # list all func for os module
    return


def dirlist():
    path = "/"
    dir_list = os.listdir(path)
    print("File and directories in ", path, "' :")
    print(dir_list)
    return


dirlist()
workingdr()
