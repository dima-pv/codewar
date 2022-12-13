# You probably know the "like" system from Facebook and other pages. People can "like" blog posts,
# pictures or other items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names):
    text_0 = " likes this"
    text_1 = " like this"
    text_2 = " others like this"
    text_3 = "no one likes this"
    if len(names) == 0:
        return text_3
    elif len(names) == 1:
        return names[0] + text_0
    elif len(names) == 2:
        return names[0] + ' and ' + names[1] + text_1
    elif len(names) == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + text_1
    elif len(names) > 3:
        return names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) +  text_2


def likes2(names):
    textToReturn = ""

    if (len(names) == 0):
        textToReturn = "no one likes this"
    elif (len(names) == 1):
        textToReturn = str(names[0]) + " likes this"
    elif (len(names) > 1 and len(names) < 4):
        for name in range(0, len(names) - 1):
            textToReturn = textToReturn + names[name] + ", "
        textToReturn = textToReturn[:-2]
        textToReturn = textToReturn + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(0, 2):
            textToReturn = textToReturn + names[name] + ", "
        textToReturn = textToReturn[:-2]
        textToReturn = textToReturn + " and " + str(len(names)-2) + " others like this"
    return textToReturn

def likes3(names):
    l = len(names)
    if l == 0: return 'no one likes this'
    if l == 1: return '{} likes this'.format(names[0])
    if l == 2: return '{} and {} like this'.format(names[0], names[1])
    if l == 3: return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    return '{}, {} and {} others like this'.format(names[0], names[1], len(names)-2)

print(likes([]))
print(likes2([]))