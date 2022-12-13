# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    split_text = text.split(' ')
    pig_sentence = ' '
    for word in split_text:
        if word in '!.%&?':
            pig_sentence = pig_sentence + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence = pig_sentence + pig_word + ' '
    return pig_sentence.strip(' ')

print(pig_it('Pig latin is cool'))




def pig_it1(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

print(pig_it1('Pig latin is cool'))