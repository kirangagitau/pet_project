#!/usr/bin/python3

''' A function to convert a given
weight into either pounds of kilograms
'''


def weight_unit():
    mass = float(input("Enter mass: "))
    choice = input(("k= kilograms, l= lb: "))
    if choice.upper() == "K":
        ''' upper() converts choice to upper case
        before doing comparison'''

        lb = mass * 2.205  # convert to pounds
        print('Mass is {:.2f}'.format(lb))
    elif choice.lower() == "l":
        kg = mass * 0.45  # convert to kg
        print('Mass is {:.2f}'.format(kg))  # formated output
    else:
        print("INVALID INPUT !!")
    return


weight_unit()  # calling the function
