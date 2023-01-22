# Define a function that takes an integer argument and returns a logical value true or false depending on
# if the integer is a prime.
#
# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive
# divisors other than 1 and itself.
#
# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
# Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */

import math


def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False

print(is_prime(-5))


def is_prime1(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a + 1
    return num > 1

print(is_prime1(14))
print(is_prime1(7))


