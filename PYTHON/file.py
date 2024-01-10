#!/usr/bin/python3

'''open a file in append mode'''
file = open("names.txt", "a+")
name = "mark"

'''using write to append a name'''
file.write(name)
file.close()
