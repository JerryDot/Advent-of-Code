import re
import numpy 
from operator import add

source_input = open("guard_record_sorted.txt")

data = source_input.readlines()
guard_timings = numpy.zeros((1110, 3), dtype=int)

#first column is time in minutes
#second column is guard id
#for the third column: 
#2 marks guard start
#1 marks fall asleep
#0 marks wake up

counter = 0
for line in data:
    x = [0] * 3
    guard_number_bool = False

    if re.search(r"#\d+", line):
        x_one = re.search(r"#\d+", line).group()
        one_x = x_one[1:]
        x[1] = int(one_x)
        x[2] = 2
        guard_number_bool = True
    else:
        x[1] = 0
        if re.search(r"asleep", line):
            x[2] = 1
        else:
            x[2] = 0

    x_zero = re.search(r":\d+", line).group()
    zero_x = x_zero[1:]
    if int(zero_x) > 30 and guard_number_bool:
        zero_x = 0
    x[0] = int(zero_x)

    guard_timings[counter] = x
    counter +=1

print(guard_timings)
guard_nights = list()
print(guard_nights)
no_of_guard_record = -1
#new_list = [0]*62

for row in guard_timings:
    print(row)
    if row[2] == 2:
        print("guard")
        if no_of_guard_record > -0.5:
            guard_nights[no_of_guard_record][61] = sum(guard_nights[no_of_guard_record][:-2])
        guard_nights.append([0]*62)
        no_of_guard_record += 1
        guard_nights[no_of_guard_record][60] = row[1]

    elif row[2] == 1:
        print("asleep")
        for i in range(row[0], 60):
            guard_nights[no_of_guard_record][i] = 1
    elif row[2] == 0:
        print("awake")
        for i in range(row[0], 60):
            guard_nights[no_of_guard_record][i] = 0

guard_nights[no_of_guard_record][61] = sum(guard_nights[no_of_guard_record][:-2])

print(guard_nights)

guard_ids = [0] * 77
guard_minutes = numpy.zeros((77, 60), dtype=int)
print(guard_minutes)
counter = 0
for row in guard_nights:
    if row[60] in guard_ids:
        minutes_index = guard_ids.index(row[60])
        for i in range(60):
            guard_minutes[minutes_index][i] += row[i]
    else:
        guard_ids[counter] = row[60]
        for i in range(60):
            guard_minutes[counter][i] += row[i]
        counter += 1

for row in guard_minutes:
    print(row)

print(guard_minutes[10][10])
max_x = 0
max_y = 0
max_number = 0
for x in range(77):
    for y in range(60):
        if guard_minutes[x][y] > max_number:
            max_x = x
            max_y = y
            max_number = guard_minutes[x][y]

print(guard_ids[max_x])
print(max_y)
print(max_number)

print(max_y*guard_ids[max_x])

#outputs the correct answer 96951