frequency = 0
source_input = open("numbers_to_sum.txt")
data = source_input.readlines()
array_of_seen_frequencies = set([0])
finished = False

def check_frequency_novelty():
    global frequency
    if frequency in array_of_seen_frequencies:
        global finished 
        finished = True
        return True
    else:
        array_of_seen_frequencies.add(frequency)
        return False

def run_through_list():
    global frequency
    for line in data:
        value = int(line)
        frequency += value
        if check_frequency_novelty():
            break

while not finished:
    run_through_list()

source_input.close()
print(frequency)

#Correct output of 558 given