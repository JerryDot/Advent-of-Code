#incomplete
import numpy
numpy.set_printoptions(threshold=numpy.nan)
environment = [[0]*(150)]*151 # dimensions can be obtained using the same loop below with environment line omitted

with open("tracks.txt") as f:
  counter_y = 0
  for line in f:
    counter_x = 0
    for character in line:
      environment[counter_x][counter_y] = character
      counter_x += 1
    counter_y += 1

print(environment)
#obtain starting cart positions:
for x in environment:
  if x == "<":
    print("hi")

#print(environment)

