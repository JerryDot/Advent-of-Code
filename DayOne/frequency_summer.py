frequency = 0
source_input = open("numbers_to_sum.txt")
data = source_input.readlines()

for line in data:
    value = int(line)
    frequency += value

source_input.close()
print(frequency)