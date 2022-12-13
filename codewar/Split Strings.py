# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing
# second character of the final pair with an underscore ('_').


def solution1(s):
    a_list = []
    result = s if len(s)%2==0 else f'{s}_'
    for e in range(0, len(result),2):
        a_list.append(result[e:e+2])
    return a_list

def solution1(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

