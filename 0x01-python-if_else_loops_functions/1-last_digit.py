#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_dgit = number % -10
else:
    last_dgit = number % 10

print("Last digit of {:d} is {:d}".format(number, last_dgit))

#print("Last digit of {:d} is {:d} and is greater than 5".format(number, lastdigit))

if last_dgit > 5:
    print("and is greater than 5")
elif last_dgit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
