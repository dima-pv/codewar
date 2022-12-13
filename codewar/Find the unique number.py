# here is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:

def find_uniq(arr):
    arr.sort()
    if arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]:
        result = arr[0]
    else:
        result = arr[len(arr)-1]
    return result

print(find_uniq([1, 1, 1, 2, 1, 1]))

def find_uniq1(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e

print(find_uniq1([1, 1, 1, 2, 1, 1]))