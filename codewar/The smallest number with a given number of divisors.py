# You have a natural number d.
#
# You need to write a function f(d) which finds the smallest positive number n having d divisors .
#
# For example:
#
# f(1) = 1
# f(3) = 4
# f(60) = 5040
# f(420) = 9979200
# In this kata all the tests will be with 1 <= d <= 10000
#
# Keep in mind that n can be on the order of 1030010^{300}10
# 300
#  , so iterating over n and finding the divisors in total for O(n(n)O(n\sqrt{\mathstrut n})O(n
# (n
# ​
#  ) operations is not an option.
#
# Good luck!

from math import isqrt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def g(n,i):
    p=primes[i]
    m=p**(n-1)
    for d in range(2,isqrt(n)+1):
        if n%d==0: m=min(m,p**(d-1)*g(n//d,i+1),p**(n//d-1)*g(d,i+1))
    return m

def f(n):return g(n,0)