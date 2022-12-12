#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for alphabets in str:
        if ord(alphabets) in range(97, 123):
            new_string += chr(ord(alphabets) - 32)
        else:
            new_string += alphabets
    print(new_string)
