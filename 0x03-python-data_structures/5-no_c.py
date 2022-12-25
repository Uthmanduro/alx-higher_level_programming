#!/usr/bin/python3
def no_c(my_string):
    mylist = list(my_string)
    for i in mylist:
        if i == "c" or i == "C":
            mylist.remove(i)
    new = "".join(mylist)
    return new
