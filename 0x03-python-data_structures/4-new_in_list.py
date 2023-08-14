#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    low = 0
    high = len(my_list) - 1
    list_copy = my_list.copy()
    if idx < low or idx > high:
        return my_list
    else:
        list_copy[idx] = element
        return list_copy
