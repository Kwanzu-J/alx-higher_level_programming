#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    low = 0
    high = len(my_list)
    if idx < low or idx > high:
        return none
    else:
        my_list[idx] = element
        return my_list
