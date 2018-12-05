f = open("polymer.txt", "r")
contents = f.read()
list_contents = list(contents)
print(list_contents)

def annihilate(letter1, letter2):
    if letter1.upper() == letter2.upper() and letter1 != letter2:
        return True
    else:
        return False

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

change_of_length_of_polymer = 1

while change_of_length_of_polymer > 0.1:

    before_length = len(list_contents)
    for x in range(len(list_contents)-1):
        if list_contents[x] == 0:
            pass
        else:
            if annihilate(list_contents[x], list_contents[x+1]):
                list_contents[x] = 0
                list_contents[x+1] = 0

    list_contents = remove_values_from_list(list_contents, 0)
    after_length = len(list_contents)
    change_of_length_of_polymer = before_length - after_length

print(len(list_contents))

#prints correct answer of 11720