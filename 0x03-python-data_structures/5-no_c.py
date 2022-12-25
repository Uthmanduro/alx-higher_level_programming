#!/usr/bin/python3
def no_c(my_string):
    mylist = []
    for i in my_string:
        if i != "c" and i != "C":
            mylist.append(i)
    new = "".join(mylist)
    return new
