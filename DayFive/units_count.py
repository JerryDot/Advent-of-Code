import string
import time

start = time.time()

iterate_alphabet = list(string.ascii_lowercase)
answer_list = [0] * 26

def annihilate(letter1, letter2):
    if letter1.upper() == letter2.upper() and letter1 != letter2:
        return True
    else:
        return False

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

counter = 0
for letter in iterate_alphabet:

    f = open("polymer.txt", "r")
    contents = f.read()
    list_contents = list(contents)

    list_contents = remove_values_from_list(list_contents, letter)
    list_contents = remove_values_from_list(list_contents, letter.upper())

    #print(list_contents)

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

    answer_list[counter] = len(list_contents)
    print(len(list_contents))

    f.close()
    counter += 1

print(min(answer_list))

#gives correct answer of 4956

end = time.time()
print(end-start)
#Took 46.5s