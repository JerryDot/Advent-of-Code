source_input = open("letter_strings.txt")
data = source_input.readlines()

def compare_two_lists(listA, listB):

    try:
        listA.remove("\n")
    except ValueError:
        pass  # do nothing!

    try:
        listB.remove("\n")
    except ValueError:
        pass  # do nothing!

    differences = 0

    # find number of differences between lists
    for x in range(len(listA)):
        if listA[x] != listB[x]:
            differences += 1
            character = listA[x]
    
    # end if solution found
    if differences == 1:
        listA.remove(character)
        print("".join(listA))
        return False
    # otherwise keep going
    else:
        return True

continue_going = True


for line in data:
    if continue_going == False:
        break
    list_one = list(line)
    for other_line in data:
        if continue_going == False:
            break
        list_two = list(other_line)
        continue_going = compare_two_lists(list_one, list_two)

#outputs correct answer qcslyvphgkrmdawljuefotxbh