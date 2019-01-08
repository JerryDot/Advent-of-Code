
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

def find_next_step_to_complete():
  for x in range(len(letter_dependencies)):
    if letter_dependencies[x] == []:
      letter_dependencies[x].append(0)
      return letter_list[x]


def clear_completed_step_from_dependencies(remove_step):
  for x in range(len(letter_dependencies)):
    if letter_dependencies[x].count(remove_step) == 1:
      letter_dependencies[x].remove(remove_step)


continue_indicator = True
while continue_indicator:
  remove_step = find_next_step_to_complete()
  if remove_step:
    answer_string = answer_string + remove_step
    clear_completed_step_from_dependencies(remove_step)
  else:
    break

print(answer_string)
#gives correct answer CFMNLOAHRKPTWBJSYZVGUQXIDE
