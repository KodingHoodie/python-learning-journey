# INSTRUCTIONS:
# Using the variables below, write conditional logic that prints:
# - "you are a master magician" if the person is both a magician AND an expert
# - "at least you're getting there" if the person is a magician but NOT an expert
# - "you need magic powers" if the person is NOT a magician
#
# This exercise practices:
# - logical operators (and / or / not)
# - combining multiple conditions
# - writing clean if/elif/else chains

is_magician = True
is_expert = False

if is_expert and is_magician:
    print("you are a master magician")

elif is_magician and not is_expert:
    print("at least you're getting there")

elif not is_magician:
    print("you need magic powers")