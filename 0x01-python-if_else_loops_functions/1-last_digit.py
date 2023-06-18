#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    dlast = ((number * -1) % 10) * -1
else:
    dlast = number % 10
if dlast > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, dlast))
elif dlast == 0:
    print("Last digit of {} is {} and is 0".format(number, dlast))
elif dlast < 6 and dlast != 0:
    print("Last digit of {} is {} and is less\
 than 6 and not 0".format(number, dlast))
