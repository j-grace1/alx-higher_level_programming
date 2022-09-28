#!/usr/bin/python3
# 10-best_score.py
def best_score(a_dictionary):
    values = []
    keys = []
    if len(a_dictionary) > 0:
        for i in a_dictionary:
            keys.append(i)
            values.append(a_dictionary[i])
        values1 = sorted(values)
        return(keys[(values.index(values1[-1]))])
    else:
        return None
