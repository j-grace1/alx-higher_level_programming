#!/usr/bin/python3
# 8-simple_delete.py
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary:
        if i == key:
            del a_dictionary[key]
    return(a_dictionary)
