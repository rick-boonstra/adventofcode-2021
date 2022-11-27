with open('06/input.txt', 'r') as inputfile:
    raw_list = inputfile.read().split(',')
    cleaned_list = [int(x) for x in raw_list]

fish_counts = [0,0,0,0,0,0,0,0,0]

for i in range(0,9):
    fish_counts[i] = cleaned_list.count(i)

def increment_day(fish_counts):
    zero_count = fish_counts[0]

    for i in range(0,8):
        fish_counts[i] = fish_counts[i + 1]
    
    fish_counts[6] += zero_count
    fish_counts[8] = zero_count    

    return fish_counts

# PART ONE

for i in range(0,80):
    fish_counts = increment_day(fish_counts)

print(sum(fish_counts))

# PART TWO

for i in range(0,176):
    fish_counts = increment_day(fish_counts)

print(sum(fish_counts))
