#!/usr/bin/python3
# 9-multiply_by_2.py
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary:
        new_dict.update({i: (a_dictionary[i])*2})
    return(new_dict)
