from signal import siginterrupt


def print_last_digit(number):
    if number < 0:
        sign = "-"
    else:
        sign = ''
    str_numb = str(number)
    last_dig = str_numb[-1]
    print(sign + last_dig)
