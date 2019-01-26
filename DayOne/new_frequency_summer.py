frequency = 0
source_input = open("numbers_to_sum.txt")
data = source_input.readlines()
array_of_seen_frequencies = set([0])
finished = False

def check_frequency_novelty(frequency):
    if frequency in array_of_seen_frequencies:
        return True
    else:
        array_of_seen_frequencies.add(frequency)
        return False

def run_through_list(frequency):
    for line in data:
        value = int(line)
        frequency += value
        if check_frequency_novelty(frequency):
            return True
        else:
            return frequency

while not finished:
    if run_through_list(frequency) == True:
        break
    else:
        frequency = run_through_list(frequency)

source_input.close()
print(frequency)

#Correct output of 558 given