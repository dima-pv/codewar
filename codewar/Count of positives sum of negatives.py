# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second
# element is sum of negative numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.

def count_positives_sum_negatives(arr):
    w = []
    q = []
    x = 0 ; z = 0
    if len(arr) == 0:
        return w
    for i in arr:
        if i < 0:
            w.append(i)
            x = sum(w)
        elif i > 0:
            q.append(i)
            z = len(q)
        else:
            x = 0; z = 0
    return [z, x]

print(count_positives_sum_negatives([]))

def count_positives_sum_negatives1(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []


print(count_positives_sum_negatives1([2,5,6,874,6,-5,-5,-4,4]))