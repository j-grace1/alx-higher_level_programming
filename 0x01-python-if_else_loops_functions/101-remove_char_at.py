#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ''
    x = str.index(str[n])
    for i in range(0, len(str)):
        if i != x:
            new_str = new_str + str[i]
        else:
            continue
    print('{}'.format(new_str), end='')
