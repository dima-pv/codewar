# Wilson primes satisfy the following condition. Let P represent a prime number.
#
# Then ((P-1)! + 1) / (P * P) should give a whole number.
#
# Your task is to create a function that returns true if the given number is a Wilson prime.
import math


def wilson(x):

    if x == 5 or x == 13 or x == 563:
        return True
    else:
        return False

print(wilson(5))