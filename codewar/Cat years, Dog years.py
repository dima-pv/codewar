# I have a cat and a dog.
#
# I got them at the same time as kitten/puppy. That was humanYears years ago.
#
# Return their respective ages now as [humanYears,catYears,dogYears]
#
# NOTES:
#
# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

def human_years_cat_years_dog_years(human_years):
    human = human_years
    cat = 15
    dog = 15
    if human_years == 1:
        cat = 15
        dog = 15
    elif human_years == 2:
        cat += 9
        dog += 9
    elif human_years >=3:
        cat = 24 + (human_years - 2) * 4
        dog = 24 + (human_years - 2) * 5
    return [human, cat, dog]

print(human_years_cat_years_dog_years(10))

# Второй вариант

def human_years_cat_years_dog_year(x):
    return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]

print(human_years_cat_years_dog_year(10))