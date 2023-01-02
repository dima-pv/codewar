# Write a function, which takes a non-negative integer (seconds) as input and returns the time in
# a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.


def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    second_ = seconds - (hours * 3600) - (minutes * 60)

    if hours < 1:
        h = '00'
    elif 1 <= hours < 10:
        h = f"0{hours}"
    else:
        h = hours

    if minutes < 1:
        m = '00'
    elif 1 <= minutes < 10:
        m = f"0{minutes}"
    else:
        m = minutes

    if second_ < 1:
        s = '00'
    elif 1 <= second_ < 10:
        s = f"0{second_}"
    else:
        s = second_

    return f'{h}:{m}:{s}'


print(make_readable(60))


def make_readable1(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


print(make_readable1(60))


def make_readable2(seconds):
    h= seconds/60**2
    m= (seconds%60**2)/60
    s= (seconds%60**2%60)
    return "%02d:%02d:%02d" % (h, m, s)


print(make_readable2(60))


