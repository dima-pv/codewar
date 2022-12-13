# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    arr = []
    arr2 = []
    n = array.count(0)
    for i in range(1, n + 1):
        arr.append(0)
    for k in array:
        if k != 0:
            arr2.append(k)
    arr2.extend(arr)
    return arr2

print(move_zeros([0, 0, 0, 5, 5]))

def move_zeros1(array) -> list:
    tmp = []
    while 0 in array:
        tmp.append(0)
        array.remove(0)
    return array + tmp

print(move_zeros1([0, 0, 0, 5, 5]))