# Let us consider this example (array written in general format):
#
# ls = [0, 1, 3, 6, 10]
#
# Its following parts:
#
# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []
# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]
#
# The function parts_sums (or its variants in other languages) will take
# as parameter a list ls and return a list of the sums of its parts as defined above.

def parts_sums0(ls):   # правильно но долго
    lst = []
    if len(ls) == 0:
        return [0]
    else:
        while len(ls) != 0:
            lst.append(sum(ls))
            ls.pop(0)
        lst.append(0)
        return lst

print(parts_sums0([1, 1, 1, 1]))


def parts_sums(ls):
    sums = [sum(ls)]
    for i in ls:
        sums.append(sums[-1]-i)
    return sums

print(parts_sums([1, 1, 1, 1]))
