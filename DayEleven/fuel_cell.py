import numpy
puzzle_input = 1308
fuel_cells = numpy.zeros((300,300), dtype=int)

for index, x in numpy.ndenumerate(fuel_cells):
    power_level = ((index[0] + 10)*index[1] + puzzle_input)*(index[0]+10)
    if power_level < 100:
        power_level = -5
    else:
        power_level = int((str(power_level))[-3]) - 5
    fuel_cells[index[0], index[1]] = power_level

print(fuel_cells)

def sum_of_cells(fuel_cells, x, y, size_of_square):
    return numpy.sum(fuel_cells[x:x+size_of_square, y:y+size_of_square])

current_meta_maximum = 0
current_meta_x = 0
current_meta_y = 0
current_optimal_square_size
for size_of_square in range(1,300):
    current_maximum = sum_of_cells(fuel_cells, 0, 0, size_of_square)
    current_max_x = 0
    current_max_y = 0
    for x in range(0,300-size_of_square):
        for y in range(0,300-size_of_square):
            if sum_of_cells(fuel_cells, x, y, size_of_square) > current_maximum:
                current_max_x = x
                current_max_y = y
                current_maximum = sum_of_cells(fuel_cells, x, y, size_of_square)

    if current_maximum > current_meta_maximum:
        current_meta_x = current_max_x
        current_meta_y = current_max_y
        current_meta_maximum = current_maximum
        current_optimal_square_size = size_of_square

print(current_meta_x, current_meta_y, current_optimal_square_size)
