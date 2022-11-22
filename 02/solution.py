with open('02/input.txt', 'r') as inputfile:
    move_list = inputfile.read().splitlines()

# PART ONE
    
x = 0
y = 0

for move in move_list:
    direction = move.split()[0]
    value = int(move.split()[1])

    if direction == 'forward':
        x = x + value
    elif direction == 'up':
        y = y - value
    elif direction == 'down':
        y = y + value

# PART TWO
        
'''
In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

'''

x = 0
y = 0
aim = 0

for move in move_list:
    direction = move.split()[0]
    value = int(move.split()[1])

    if direction == 'forward':
        x = x + value
        y = y + (aim * value)
    elif direction == 'up':
        aim = aim - value
    elif direction == 'down':
        aim = aim + value

print(f'{x}, {y}: {x * y}')
