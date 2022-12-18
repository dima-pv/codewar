# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
# A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]
# Go challenge Build Tower Advanced once you have finished this :)

def tower_builder(n_floor):
    result = []
    item = (n_floor * 2) - 1
    for x in range(1, 2 * n_floor, 2):
        stars = x * '*'
        line = stars.center(item)
        result.append(line)
    return result

print(tower_builder(3))

def tower_builder1(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

print(tower_builder1(3))