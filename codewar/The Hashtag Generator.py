# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    res_ = s.title().split()
    res = ''.join(res_)
    if 0 < len(res) <= 140:
        return f'#{res}'
    else:
        return False


print(generate_hashtag('codewars is nice'))


def generate_hashtag1(s):
    output = "#"
    for word in s.split():
        output += word.capitalize()
    return False if (len(s) == 0 or len(output) > 140) else output


print(generate_hashtag1('codewars is nice'))


def generate_hashtag2(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False


print(generate_hashtag2('codewars is nice'))