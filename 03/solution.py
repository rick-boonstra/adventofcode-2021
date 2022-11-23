import copy
import statistics

with open('03/input.txt', 'r') as inputfile:
    raw_list = inputfile.read().splitlines()
    diagnostic_list = [x.strip() for x in raw_list]

# PART ONE

'''
Each bit in the gamma rate can be determined by finding the most common bit in 
the corresponding position of all numbers in the diagnostic report.

The epsilon rate is calculated in a similar way; rather than use the most common 
bit, the least common bit from each position is used.

Use the binary numbers in your diagnostic report to calculate the gamma rate and 
epsilon rate, then multiply them together.
'''

element_lists = []
size = len(diagnostic_list[0]) # assumes that all elements have the same length

for i in range(0, size): 
    element_lists.append([])

for value in diagnostic_list:
    for position, character in enumerate(value):
        element_lists[position].append(int(character))

gamma = ''
epsilon = ''

for i in range(0, size):
    if statistics.median(element_lists[i]) == 0.0:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    else:
        gamma = gamma + '1'
        epsilon = epsilon + '0'

print(f'{int(gamma, 2)} {int(epsilon, 2)} {int(gamma, 2) * int(epsilon, 2)}')

# PART TWO

'''
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit 
position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, 
keep values with a 1 in the position being considered.

To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, 
and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values 
with a 0 in the position being considered.
'''

o2_list = copy.deepcopy(diagnostic_list)
co2_list = copy.deepcopy(diagnostic_list)

for i in range(0, size):
    o2_currentvalues = [int(x[i]) for x in o2_list]
    o2_median = statistics.median(o2_currentvalues)

    if (o2_median == 1.0 or o2_median == 0.5) and len(o2_list) > 1:
        o2_list = [x for x in o2_list if x[i] == '1']
    elif len(o2_list) > 1:
        o2_list = [x for x in o2_list if x[i] == '0']
        
    co2_currentvalues = [int(x[i]) for x in co2_list]
    co2_median = statistics.median(co2_currentvalues)

    if (co2_median == 1.0 or co2_median == 0.5) and len(co2_list) > 1:
        co2_list = [x for x in co2_list if x[i] == '0']
    elif len(co2_list) > 1:
        co2_list = [x for x in co2_list if x[i] == '1']

o2_value = int(o2_list[0], 2)
co2_value = int(co2_list[0], 2)

print(f'{o2_value} {co2_value} {o2_value * co2_value}')
