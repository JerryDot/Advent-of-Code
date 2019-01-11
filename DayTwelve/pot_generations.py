initial_state = ".##..##..####..#.#.#.###....#...#..#.#.#..#...#....##.#.#.#.#.#..######.##....##.###....##..#.####.#" #length is 100
rules = dict()

with open("input.txt") as f:
  counter = 0
  for line in f:
    if counter >= 2:
      rule = []
      for thing in line.split(" "):
        rule.append(thing)
      rules[str(rule[0])] = str(rule[2][0])
    counter += 1

#create environment of 50 . then the initial_state, then 200 .
upper_limit = 10000
environment = ["."]*upper_limit
for index, character in enumerate(initial_state):
  environment[index + 50] = character
#print(environment)

def one_generation_on(environment, rules):
  new_environment = environment.copy()
  for environment_index in range(2,upper_limit-2):
    new_environment[environment_index] = rules["".join(environment[(environment_index-2):(environment_index+3)])]
  return new_environment

def check_boundaries_safe(environment):
  if environment[2] == "#":
    return "lower boundary unsafe"
  elif environment[upper_limit-3] == "#":
    return "upper boundary unsafe"

generations = 500
for x in range(1, generations):
  environment = one_generation_on(environment,rules)
  if check_boundaries_safe(environment):
    print(check_boundaries_safe(environment))
  sum = 0
  for index, pot in enumerate(environment):
    if pot == "#":
      sum += (index-50)
  print(x, sum)

# observe that output tends to adding 58 to the total on each generation
# for generation 400 the sum is 25056

generation_fifty_billion = 25056 + 58*(50000000000-400)
print(generation_fifty_billion)




