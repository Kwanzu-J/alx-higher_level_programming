#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_keys = list(a_dictionary.keys())
    for i in new_keys:
        a_dictionary[i] *= 2
    return (a_dictionary)
