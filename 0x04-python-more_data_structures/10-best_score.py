#!/usr/bin/python3
# 10-best_score.py
def best_score(a_dictionary):
    if len(a_dictionary) > 0:
        return(sorted(a_dictionary.values)[-1])
    else:
        return None
