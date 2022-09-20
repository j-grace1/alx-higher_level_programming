
import random
number = random.randint(-10000, 10000)
if number < 0:
    sign = '-'
else:
    sign = ''
number = str(number)
last = (number[-1])
last = int(last)

if last == 0:
    print(f"Last digit of {number} is {sign}{last} and is 0")
elif last < 6:
    print(f"Last digit of {number} is {sign}{last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {sign}{last} and is greater than 5")

