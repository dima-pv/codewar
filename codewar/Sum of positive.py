# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.
arr = []
x = []
def positive_sum(arr):
    for i in arr:
        if i > 0:
            x.append(i)
        else:
            i = 0
            x.append(i)
    return sum(x)

print(positive_sum([1,2,3]))

def positive_sum1(arr1):
    return sum(x for x in arr1 if x > 0)

print(positive_sum1([1,2,3]))
