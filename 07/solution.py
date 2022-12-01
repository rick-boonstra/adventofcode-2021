import numpy as np

with open('07/input.txt', 'r') as inputfile:
    raw_list = inputfile.read().split(',')
    cleaned_list = [int(x) for x in raw_list]

count_list = []
max_pos = max(cleaned_list)
    
for i in range(0, max_pos + 1):
    count_list.append(cleaned_list.count(i))

crab_position_counts = np.array(count_list)

# PART ONE

distances_list = []

for i in range(0, len(crab_position_counts)):
    distance_per_position = np.array([abs(x - i) for x in range(0, len(crab_position_counts))])
    distances_times_crabs = crab_position_counts * distance_per_position
    total_distance = np.sum(distances_times_crabs)
    distances_list.append(total_distance)

print(min(distances_list))

# PART TWO

distances_list = []

for i in range(0, len(crab_position_counts)):

    distance_per_position = np.array([(abs(x - i) * (abs(x - i) + 1)) / 2 for x in range(0, len(crab_position_counts))])
    distances_times_crabs = crab_position_counts * distance_per_position
    total_distance = np.sum(distances_times_crabs)
    distances_list.append(total_distance)

print(min(distances_list))
