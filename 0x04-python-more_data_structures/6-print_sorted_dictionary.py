def print_sorted_dictionary(a_dictionary):
    new_dict = {}
    for i in sorted(a_dictionary):
        new_dict.update({i: a_dictionary[i]})
    return(new_dict)
