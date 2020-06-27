# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.


string_input = input('Enter a string : ')

string_lenght = len(string_input)

first_char = string_input[0]
last_char = string_input[-1]


changed_string = last_char+string_input[1:(string_lenght-1)]+first_char

print(f'Result after swapping first and last character : {changed_string}')

# OUTPUT

# Enter a string : python assignment
# Result after swapping first and last character : tython assignmenp
