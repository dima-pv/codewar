# Your boss decided to save money by purchasing some cut-rate optical
# character recognition software for scanning in the text of old novels to your database.
# At first it seems to capture words okay, but you quickly notice that it throws in a lot
# of numbers at random places in the text.
# Your harried co-workers are looking to you for a solution to take this garbled text
# and remove all of the numbers. Your program will take in a string and clean out all numeric characters,
# and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.

def del_num(text):
    rtrn = ''
    for i in text:
        if not i.isdigit():
            rtrn += i
    return rtrn

print(del_num('(E3at m2e2!!)'))

def string_clean(s):
    str2 = ''
    for i in s:
        if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            str2 += i
    return str2

print(string_clean('(E3at m2e2!!)'))

# str1='112 sadd dfdf 21 dfheif 1223 12'
# str2=''
# for c in str1:
#    if c not in ('0','1','2','3','4','5','6','7','8','9'):
#       str2=str2+c
#
# print(str2)