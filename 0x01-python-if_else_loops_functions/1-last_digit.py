#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_dgit = number % -10
else:
    last_dgit = number % 10

if last_dgit > 5:
    print("Last digit of", number, "is", last_dgit, "and is greater than 5")
elif last_dgit == 0:
    print("Last digit of", number, "is", last_dgit, "and is 0")
else:
    print("Last digit of", number, "is", last_dgit,
          "and is less than 6 and not 0")
