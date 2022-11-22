import numpy as np

with open('01/input.txt', 'r') as inputfile:
    depth_list = inputfile.read().splitlines()

# PART ONE

increase_count = 0

for i in range(1,len(depth_list)):
    if int(depth_list[i]) > int(depth_list[i - 1]):
        increase_count += 1

print(increase_count)

# PART TWO

increase_count_window = 0

for i in range(3,len(depth_list)):
    current_window = int(depth_list[i])
    prior_window = int(depth_list[i - 3])
    if current_window > prior_window:
        increase_count_window += 1

print(increase_count_window)
