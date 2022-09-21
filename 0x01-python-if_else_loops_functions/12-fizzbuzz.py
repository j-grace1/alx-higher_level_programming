#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i >= 3 and i % 3 == 0 and i % 15 != 0:
            print("{}".format('Fizz'), end=' ')
        elif i >= 5 and i % 5 == 0 and i % 15 != 0:
            print("{}".format('Buzz'), end=' ')
        elif i >= 15 and i % 15 == 0:
            print("{}".format('FizzBuzz'), end=' ')
        else:
            print("{}".format(i), end=' ')
