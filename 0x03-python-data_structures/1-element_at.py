#!/usr/bin/python3
def element_at(my_list, idx):
    low = 0
    high = len(my_list) - 1
    if idx < low or idx > high:
        return none
    else:
        return my_list[idx]
