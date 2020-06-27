# 11. Write a Python program to count the occurrences of each word in a given
# sentence


string_input = input(' ENTER ANY SENTENCE: ')

input_list = string_input.lower().split()

list_dictionary = dict((i, input_list.count(i)) for i in input_list)


for k, v in list_dictionary.items():
    print(f'{k} : {v}')

# OUTPUT

# ENTER ANY SENTENCE: I have been doing the assignment that has been the second assignment in the assignment list

# i : 1
# have : 1
# been : 2
# doing : 1
# the : 3
# assignment : 3
# that : 1
# has : 1
# second : 1
# in : 1
# list : 1
