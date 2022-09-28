#!/usr/bin/python3
# 0-square_matrix_simple.py
def best_score(a_dictionary):
    if len(a_dictionary) > 0:
        for i in a_dictionary:
            if i == (sorted(a_dictionary.values)[-1]):
                return(i)
            else:
                continue
    else:
        return None
best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10})
