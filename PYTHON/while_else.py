#!/usr/bin/python3

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    print("outside the loop now")
print('code proceeds here')
