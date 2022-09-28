#!/usr/bin/python3
# 7-update-dictionary.py
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary:
        if key == a_dictionary[i]:
            a_dictionary[i] = value
        else:
            a_dictionary.update({key: value})