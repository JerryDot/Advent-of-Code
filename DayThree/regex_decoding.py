import re
import numpy 

source_input = open("fabric_claims.txt")

data = source_input.readlines()
claims_array = numpy.zeros((1287, 5))
counter = 0
for line in data:

    x = [0] * 5

    x_zero = re.match(r"\#\d+", line).group()
    x[0] = int(x_zero[1:])
    x_one = re.search(r"([0-9])+,", line).group()
    x[1] = int(x_one[:-1])
    x_two = re.search(r",\d+", line).group()
    x[2] = int(x_two[1:])
    x_three = re.search(r"\d+x", line).group()
    x[3] = int(x_three[:-1])
    x_four = re.search(r"x\d+", line).group()
    x[4] = int(x_four[1:])

    claims_array[counter] = x
    counter +=1

print (claims_array)

fabric_array = numpy.zeros((1000,1000))

# 30 @ 230,473: 10x27
for row in claims_array:
    x_offset = row[1]
    y_offset = row[2]
    x_size = row[3]
    y_size = row[4]
    for across in range(int(x_size)):
        for up in range(int(y_size)):
            fabric_array[int(y_offset)+up][int(x_offset)+across] += 1

number_of_zeros = 1000000 - numpy.count_nonzero(fabric_array)
matrix_of_ones = numpy.ones((1000,1000))
fabric_array_minus_one = numpy.subtract(fabric_array, matrix_of_ones)
number_of_ones = 1000000 - numpy.count_nonzero(fabric_array_minus_one)

number_of_multiples = 1000000 - number_of_ones - number_of_zeros
print(number_of_multiples)

#output is correct answer 105047