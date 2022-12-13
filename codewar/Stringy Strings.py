# write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
#
# the string should start with a 1.
#
# a string with size 6 should return :'101010'.
#
# with size 4 should return : '1010'.
#
# with size 12 should return : '101010101010'.
#
# The size will always be positive and will only use whole numbers.

def stringy(size):
    w = []
    r = []
    for i in range(1, size+1):
        w.append(i)
    for n in w:
        if n % 2 == 0:
            r.append(0)
        else:
            r.append(1)

    return ''.join(map(str, r))

print(stringy(3))


def stringy1(size):
    return "".join([str(i % 2) for i in range(1, size + 1)])

print(stringy1(3))