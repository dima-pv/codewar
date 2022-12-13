# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    txt = str(num)
    list = []
    for i in txt:
        list.append(str(int(i)**2))
        result = ''.join(list)
    return int(result)

print(square_digits(9119))


def square_digits1(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

print(square_digits1(9119))

def square_digits2(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits2(9119))