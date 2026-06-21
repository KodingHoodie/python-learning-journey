# CPD Course Exercise: Picture Display
# INSTRUCTIONS:
# Given a 2D list of 0s and 1s, display an image in the console.
# - 0 should be printed as a space " "
# - 1 should be printed as an asterisk "*"
# This exercise practices:
# - nested loops
# - iterating through 2D lists (lists of lists)
# - conditional printing
# - using end="" to control print formatting

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,1,1,1,0,0],
    [0,0,1,0,1,0,0]
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
