# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.
from collections import Counter

def count(string):
    sp = []
    for i in string:
        sp.append(i)
    res = Counter(sp)
    return res


print(count('aba'))


def count1(string):
    return {i: string.count(i) for i in string}


print(count1('aba'))