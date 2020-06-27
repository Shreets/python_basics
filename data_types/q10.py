# 10. Write a Python program to remove the characters which have odd index
# values of a given string.

string_input = input('Enter a string : ')

string_length = len(string_input)

even_indexed_string = string_input[0:string_length:2]

print(
    f'Resul after removal of odd indexed characters are : {even_indexed_string}')

# OUTPUT

# Enter a string : Assignment
# Resul after removal of odd indexed characters are : Asgmn
