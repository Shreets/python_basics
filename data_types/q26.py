# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


input_item = input('Enter list items separated by space : ')
list_item = input_item.split()

print(list_item)

string_input = input('Enter string you want in beggining of list items : ')

new_list = []

for i in list_item:
    new_string = string_input + i
    new_list.append(new_string)


print(f'The new list is  : {new_list}')

# OUTPUT

# Enter list items separated by space : a b c d e

# ['a', 'b', 'c', 'd', 'e']

# Enter string you want in beggining of list items : group-

# The new list is  : ['group-a', 'group-b', 'group-c', 'group-d', 'group-e']
