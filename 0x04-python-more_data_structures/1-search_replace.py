#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for item in my_list:
        if item == search:
            item = replace
            new.append(replace)
            continue
        new.append(item)
    return new
