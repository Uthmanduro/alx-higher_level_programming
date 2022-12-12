#!/usr/bin/python3
for num1 in range(0, 100):
    if num1 == 99:
        print(num1)
    else:
        print("{0:02d}, ".format(num1), end="")
