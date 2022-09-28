#!/usr/bin/python3
# 2-uniq_add.py
def uniq_add(my_list=[]):
    sorted = set(my_list)
    y = 0
    for i in sorted:
        y = y + i
    return y
