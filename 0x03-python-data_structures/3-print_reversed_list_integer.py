#!/usr/bin/python3
#print_reversed_list_integer
def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list[::-1]
    for i in reversed_list:
        print("{:d}".format(i))
