# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
# anything but exactly 4 digits or exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.


def validate_pin(pin):
    lettrs_in_pin = str(pin)
    p = list(lettrs_in_pin)
    if not lettrs_in_pin.isdigit():
        return False
    elif len(p) == 4 or len(p) == 6:
        return True
    else:
        return False

print(validate_pin(55555))


def validate_pin1(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin1(55555))