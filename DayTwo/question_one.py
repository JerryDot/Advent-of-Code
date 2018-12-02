source_input = open("letter_strings.txt")
data = source_input.readlines()

number_of_doubles = 0
number_of_triples = 0

for line in data:
    listline = list(line)
    setline = set(listline)
    able_to_change_doubles = True
    able_to_change_triples = True
    for character in setline:
        number_of_instances = listline.count(character)
        print(character)
        print(number_of_instances)
        if number_of_instances == 2 and able_to_change_doubles:
            number_of_doubles += 1
            able_to_change_doubles = False
        elif number_of_instances == 3 and able_to_change_triples:
            number_of_triples +=1
            able_to_change_triples = False
        print(number_of_doubles)
        print(number_of_triples)
    
print((number_of_doubles*number_of_triples))
source_input.close()
