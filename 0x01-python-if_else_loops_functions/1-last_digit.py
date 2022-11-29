#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if (number < 0):
    last = (abs(number) % 10) * -1
else:
    last = number % 10
if (last == 0):
    ending = "and is 0"
elif (last > 5):
    ending = "and is greater than 5"
else:
    ending = "and is less than 6 and not 0"
print("Last digit of {} is {}".format(number, last), ending)
