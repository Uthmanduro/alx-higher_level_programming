#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(0, 10):
        if num1 == 9 and num2 == 9:
            print("99")
        print("{}{}, ".format(num1, num2), end="")
