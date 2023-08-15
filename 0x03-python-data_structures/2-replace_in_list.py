#!/usr/bin/python3
# replace list function
def replace_in_list(my_list, idx, element):
    low = 0
    high = len(my_list) - 1
    if (idx < low or idx > high):
        return my_list
    else:
        my_list[idx] = element
    return my_list
