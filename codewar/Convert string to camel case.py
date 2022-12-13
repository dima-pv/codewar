# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
from re import sub

def to_camel_case(text):
  text = sub(r"(_|-)+", " ", text).title().replace(" ", "")
  return ''.join([text[0].lower(), text[1:]])

print(to_camel_case('the_stealth_warrior'))


def to_camel_case1(text):
    list = [x for x in text]
    if len(list) != 0:
        for i in range(len(list)):
            if list[i] in ('-', '_'):
                list[i + 1] = list[i + 1].upper()
    list = ''.join([i for i in list if i not in ('-', '_')])
    return list

print(to_camel_case1('the_stealth_warrior'))


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])