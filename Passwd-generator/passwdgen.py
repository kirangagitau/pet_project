#!/usr/bin/python3
import random
#the password will include uppercase,lowercase,digits and symbols
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
symbols = "!@#$%^&*({}?//><"
upper, lower, nums,syms = True, True, True, True
#the variables stated above will be included in the password because of the Boolean true
all =""
#start a if loop to include all the characters in the password
if upper:
    all+=uppercase_letters
    if lower:
        all+=uppercase_letters.lower()
        if nums:
            all+=digits
            if syms:
                all+=symbols
                #specify the length of the password
                len = 8
                #specify the amount of passwords to be generated
<<<<<<< HEAD:Passwd-generator/passwordgenerator.py
                amount = 10
=======
                amount = 7
>>>>>>> fd2127c03e0129ffe74be8a3a5b6074ae0cd913b:Passwd-generator/passwdgen.py
                for x in range(amount):
                 password = "".join(random.sample(all, len))
                 print(password)
