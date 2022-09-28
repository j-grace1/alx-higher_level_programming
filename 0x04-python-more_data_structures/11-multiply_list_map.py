#!/usr/bin/python3
# 11-multipy_list_map.py
def multiply_list_map(my_list=[], number=0):
    return([list(map(lambda number: x * number, my_list)) for x in my_list])
