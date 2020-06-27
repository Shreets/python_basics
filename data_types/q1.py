# 1. Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
# #

string_input = input("Please Enter a String : ")

string_list = list(string_input.lower().replace(" ", ""))

print(f'List of characters :\n {string_list}')

result = dict((i, string_list.count(i)) for i in string_list)

print(f'the total count in characters are : \n {result}')


# OUTPUT :

# Please Enter a String : My name is Shreeti

# List of characters :
#  ['m', 'y', 'n', 'a', 'm', 'e', 'i', 's', 's', 'h', 'r', 'e', 'e', 't', 'i']

# the total count in characters are :
#  {'m': 2, 'y': 1, 'n': 1, 'a': 1, 'e': 3, 'i': 2, 's': 2, 'h': 1, 'r': 1, 't': 1}
