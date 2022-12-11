#!/usr/bin/python3
for num1 in range(0, 100):
    if num1 in range(0, 10):
        print("0", end="")
    if num1 == 99:
        print(num1)
    print("{}, ".format(num1), end="")
