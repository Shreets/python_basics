# 8. Write a Python program to remove the nth index character from a nonempty string.


string_input = input('Enter a string : ')

index_input = input('Enter index of string you want to remove : ')

nth = int(index_input)

new_string = ''

if string_input:
    nth_string = string_input[nth]
    first_string = string_input[:nth]
    last_string = string_input[nth+1:]
    new_string = first_string+last_string
else:
    print('String value empty. try again')

print(
    f"The resul after removing {index_input}th index character '{nth_string}' is : \n {new_string} ")

# OUTPUT

# Enter a string : Python

# Enter index of string you want to remove : 3

# The resul after removing 3th index character 'h' is :
#  Pyton
