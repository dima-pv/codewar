# Given a random non-negative number,
# you have to return the digits of this number
# within an array in reverse order.

def digitize(n):
    b = [int(i) for i in str(n)]
    c = list(reversed(b))
    return c

def digitiz(n):
    return [int(i) for i in str(n)][::-1]
print(digitize(123546))
print(digitiz(123546))

# def digitize(n):
#     return [int(i) for i in str(n)]
#
# print(digitize(123546))

x = 1234

# result = []
# while x > 0:
#     result.append(x % 10)
#     x //= 10
#
# # result.reverse()
# print(result)