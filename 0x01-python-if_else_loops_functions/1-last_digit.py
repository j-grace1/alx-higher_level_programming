#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    s = '-'
else:
    s = ''
number = str(number)
last = (number[-1])
last = int(last)

if last == 0:
    print(f"Last digit of {number} is {s}{last} and is 0")
elif last < 6 or number < 0:
    print(f"Last digit of {number} is {s}{last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {s}{last} and is greater than 5")

