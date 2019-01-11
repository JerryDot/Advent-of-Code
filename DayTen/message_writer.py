
import matplotlib.pyplot

particle_list =[]

#note that the split method does remove newline characters!

with open("input_particles.txt") as f:
  for line in f:
    new_particle= []
    for things in line.split(" "):
      try:
        new_things = things[:-1]
        if len(new_things) > 11:
          newer_things = new_things[10:]
        else:
          if new_things[-1:] == ">":
            newer_things = new_things[:-1]
          else:
            newer_things = new_things
        new_particle.append(int(newer_things))
      except ValueError:
        pass
    particle_list.append(new_particle)

print(particle_list)

def update_one_time_increment(particle_list):
  for particle in particle_list:
    particle[0] += particle[2]
    particle[1] += particle[3]
  return particle_list

def undate_one_time_increment(particle_list):
  for particle in particle_list:
    particle[0] -= particle[2]
    particle[1] -= particle[3]
  return particle_list


def horizontal_distance(particle_list):
  return max(particle_list[x][0] for x in range(len(particle_list)))


old_distance = 100000
counter = 0
while True:
  particle_list = update_one_time_increment(particle_list)
  distance = horizontal_distance(particle_list)
  if distance > old_distance:
    break
  else:
    old_distance = distance
  counter += 1

print(counter)
particle_list = undate_one_time_increment(particle_list)
x = [particle_list[t][0] for t in range(len(particle_list))]
y = [particle_list[t][1] for t in range(len(particle_list))]
matplotlib.pyplot.scatter(x,y)
matplotlib.pyplot.show()


