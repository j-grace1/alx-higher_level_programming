#!/usr/bin/python3
# 1-search_replace.py
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print('{}: {}'.format(i, a_dictionary[i]))
