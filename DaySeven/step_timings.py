
#assume that all letters are represented in steps
letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letter_dependencies = [[] for _ in range(len(letter_list))]

#parse input instructions into a list of dependecies for each step aka letter
with open("instructions.txt") as f:
  for line in f:
    letter_rule = ''.join([c for c in line[1:] if c.isupper()])
    letter_number = letter_list.index(letter_rule[1])
    letter_dependencies[letter_number].append(letter_rule[0])

answer_string = "The answer is: "

max_worker_time = 5000
worker1 = [0]*max_worker_time
worker2 = [0]*max_worker_time
worker3 = [0]*max_worker_time
worker4 = [0]*max_worker_time
worker5 = [0]*max_worker_time
worker_dict = {
  "worker1": worker1,
  "worker2": worker2,
  "worker3": worker3, 
  "worker4": worker4, 
  "worker5": worker5
}

def which_workers_are_available(time_tick):
  available_workers = []
  for key, value in worker_dict.items():
    if value[time_tick] == 0:
      available_workers.append(key)
  return available_workers

def find_next_steps_to_complete():
  available_steps = []
  for x in range(len(letter_dependencies)):
    if letter_dependencies[x] == []:
      available_steps.append(letter_list[x])
  return available_steps

def allocate_task(n, available_steps, available_workers):
  for allocations in range(n):
    for x in range(letter_list.index(available_steps[allocations]) + 60 + 1):
      worker_dict[available_workers[allocations]][time_tick + x] = available_steps[allocations]

def mark_tasks_as_complete_or_underway(n, available_steps):
  for allocations in range(n):
    letter_dependencies[letter_list.index(available_steps[allocations])].append(0)


def consolidate_completed_steps_from_dependencies(time_tick):
  for value in worker_dict.items():
    if value[1][time_tick] == 0 and value[1][time_tick - 1] != 0:
      clear_completed_step_from_dependencies(value[1][time_tick - 1])

def clear_completed_step_from_dependencies(remove_step):
  for x in range(len(letter_dependencies)):
    if letter_dependencies[x].count(remove_step) == 1:
      letter_dependencies[x].remove(remove_step)

time_tick = 0
continue_indicator = True
while continue_indicator:
  available_workers = which_workers_are_available(time_tick)
  available_steps = find_next_steps_to_complete()
  if len(available_workers) == 5 and len(available_steps) == 0:
    continue_indicator = False
    break

  number_of_tasks_to_allocate = min(len(available_workers), len(available_steps))
  for n in range(number_of_tasks_to_allocate):
    allocate_task(n+1, available_steps, available_workers)
    mark_tasks_as_complete_or_underway(n+1, available_steps)

  time_tick += 1
  consolidate_completed_steps_from_dependencies(time_tick)


print(time_tick)
# gives correct answer 971
