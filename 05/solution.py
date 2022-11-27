'''
To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. 
In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
'''

with open('05/input.txt', 'r') as inputfile:
    raw_list = inputfile.read().splitlines()


'''
Store board as a dictionary with key: (x, y) and value: count
'''

# PART ONE

coordinate_dict = {}

# For each line:
for line in raw_list:
    x1 = int(line.split(' -> ')[0].split(',')[0])
    x2 = int(line.split(' -> ')[1].split(',')[0]) 
    y1 = int(line.split(' -> ')[0].split(',')[1]) 
    y2 = int(line.split(' -> ')[1].split(',')[1]) 

    rise = y2 - y1
    run = x2 - x1

    distance = max(abs(rise), abs(run))

    x_step = run / distance
    y_step = rise / distance

    if rise == 0 or run == 0:
        point_list = [(x1 + (x_step * n), y1 + (y_step * n)) for n in range(0, distance + 1)]
        for point in point_list:
            if point not in coordinate_dict:
                coordinate_dict[point] = 0
            coordinate_dict[point] += 1

overlap_dict = {key:value for (key,value) in coordinate_dict.items() if value > 1}
print(len(overlap_dict))

# PART TWO

coordinate_dict = {}

# For each line:
for line in raw_list:
    x1 = int(line.split(' -> ')[0].split(',')[0])
    x2 = int(line.split(' -> ')[1].split(',')[0]) 
    y1 = int(line.split(' -> ')[0].split(',')[1]) 
    y2 = int(line.split(' -> ')[1].split(',')[1]) 

    rise = y2 - y1
    run = x2 - x1

    distance = max(abs(rise), abs(run))

    x_step = run / distance
    y_step = rise / distance

    point_list = [(x1 + (x_step * n), y1 + (y_step * n)) for n in range(0, distance + 1)]
    for point in point_list:
        if point not in coordinate_dict:
            coordinate_dict[point] = 0
        coordinate_dict[point] += 1

overlap_dict = {key:value for (key,value) in coordinate_dict.items() if value > 1}
print(len(overlap_dict))
