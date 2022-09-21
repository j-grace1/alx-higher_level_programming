from signal import siginterrupt
from unicodedata import digit


#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        sign = "-"
    else:
        sign = ''
    str_numb = str(number)
    last_digit = str_numb[-1]
    print("{}{}".format(sign, last_digit))
