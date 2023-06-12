#!/usr/bin/python3
def print_reversed_list_integer(ama_list=[]):
    if ama_list:
        ama_list.reverse()
        for i in range(len(ama_list)):
            print("{:d}".format(ama_list[i]))

