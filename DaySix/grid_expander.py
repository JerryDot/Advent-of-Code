import re
import numpy
import random
numpy.set_printoptions(threshold=numpy.inf)

source_input = open("coordinates.txt")

data = source_input.readlines()
coordinates = [0] * 50
grid = numpy.zeros((400, 400), dtype=int)

counter = 0
for line in data:

    x = [0] * 2

    x_zero = re.match(r"\d+,", line).group()
    x[0] = int(x_zero[:-1])
    x_one = re.search(r" \d+", line).group()
    x[1] = int(x_one[1:])

    coordinates[counter] = x
    counter +=1
source_input.close()

print(coordinates)

def surrounding_points(x,y):
    return [grid[x+1][y], grid[x-1][y], grid[x][y+1], grid[x][y-1]]

point_counter = 1    #note the points are going to be 1-indexed
for point in coordinates:
    grid[point[0]][point[1]] = point_counter
    point_counter += 1

while numpy.count_nonzero(grid) > 0 and numpy.count_nonzero(grid) < 158404:
    print(numpy.count_nonzero(grid))
    new_grid = numpy.copy(grid)
    for x in range(398):
        for y in range(398):
            surround = surrounding_points(x+1, y+1)
            if grid[x+1][y+1] > 0:
                pass
            elif sum(surround) > 0:
                if len(set(surround)) > 2:
                    new_grid[x+1][y+1] = random.randint(100,1000000)
                else:
                    new_grid[x+1][y+1] = max(surround)
            else:
                pass
    grid = numpy.copy(new_grid)
    #if numpy.count_nonzero(grid) == 120690:
    #   for row in grid:
    #        print(row)
    #    break

    

for row in grid:
    print(row)

unique_elements, counts_elements = numpy.unique(grid, return_counts=True)
print(numpy.asarray((unique_elements, counts_elements)))

counter = 0
for row in grid:
    if counter == 1:
        print(row)
    elif counter < 398:
        print(row[1])
        print(row[398])
    elif counter == 398:
        print(row)
    counter +=1

    
[   #1281   #4051   #2730   #3388    515   #7701    820   2170   2580
    1330   1182    #699   1557   #4222   #3526   #7026   #2738   #1909   #9329
    #5799   #4412   2377   1049   2148   2922   1265   5081   #5325   2031
    #5714   3723   #4812   #4344    900   #2683   2939    343   4813   #2948
    1034   #2096   5058   #1161    562    251   1338   #9729   #2541   1293
    2889