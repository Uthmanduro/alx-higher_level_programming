#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    for number in range(len(list_of_integers)):
        if (list_of_integers[number - 1] <= list_of_integers[number]
                and list_of_integers[number + 1] >= list_of_integers[number]):
            return list_of_integers[number]
        else:
            return max(list_of_integers)
