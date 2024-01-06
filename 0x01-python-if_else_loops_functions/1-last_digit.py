#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dgit = abs(number) % 10

print("Last digit of", number, "is", last_dgit)

if number < 0:
    last_dgit = number % -10
else:
    last_dgit = number % 10

if last_dgit > 5:
    print(f"and is greater than 5")
elif last_dgit == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
