# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with
#     the weights of members is published and each month he is the last on the list which means he is the heaviest.
#
# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list".
# It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
#
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
#
# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights"
# of these numbers?
#
# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
#
# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:
#
# 180 is before 90 since, having the same "weight" (9), it comes before as a string.
#
# All numbers in the list are positive numbers and the list can be empty.


def order_weight(strng):

    def count_weight(strng):
        return (sum(int(c) for c in strng), strng)

    return ' '.join(sorted(strng.split(' '), key=count_weight))


print(order_weight('2000 10003 1234000 44444444 9999 11 11 22 123'))


def order_weight1(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))


print(order_weight1('2000 10003 1234000 44444444 9999 11 11 22 123'))


# variant №3
def sum_string2(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum


def order_weight2(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string2))

    return result


print(order_weight2('2000 10003 1234000 44444444 9999 11 11 22 123'))
