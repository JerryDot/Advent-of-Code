import re
import numpy 

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
right_guard = False
for row in guard_timings:
    if row[1] == 3371:
        right_guard = True
    elif row[1] == 0:
        pass
    else:
        right_guard = False

    if right_guard:
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

minute_count = list(range(60))
minute_sum = [0]*60
for night in guard_nights:
    for i in range(60):
        minute_sum[i] += night[i]

print(minute_count)
print(minute_sum)
print(minute_sum.index(14))
#can read off the most common minute is 38

# answer is 3371*39 = 131469

