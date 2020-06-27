# 4. Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


string_name = input('Give me two strings separated by a space : ')

[first_str, second_str] = string_name.split()

first_modified = first_str[:(len(first_str)-1)] + second_str[-1]
second_modified = second_str[:(len(second_str)-1)] + first_str[-1]

final = first_modified + ' ' + second_modified

print(f'The new word is : {final}')

# output

# Give me two strings separated by a space : hello shreeti
# The new word is : helli shreeto
