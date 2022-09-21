#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for i in range(0, len(str)):
        x = ord(str[i])
        if x < 124 and x > 96:
            y = x - 97
            new_str = new_str + chr(y + 65)
        else:
            new_str = new_str + str[i]
    print("{}".format(new_str))
