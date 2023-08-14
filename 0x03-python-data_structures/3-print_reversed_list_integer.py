#!/usr/bin/python3
#print_reversed_list_integer
def print_reversed_list_integer(my_list=[]):
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
