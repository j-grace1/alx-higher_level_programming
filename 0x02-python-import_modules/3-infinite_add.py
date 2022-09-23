#!/usr/bin/python3
str = str(input(''))
split_str = str.split(' ')
result = 0
for i in split_str:
    result += int(i)
print('{}'.format(result))