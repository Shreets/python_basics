# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


string_input = input('Enter a word : ')

if len(string_input) < 3 or string_input[-2:] == 'ly':
    new_word = string_input
elif string_input[-3:] == 'ing':
    new_word = string_input+'ly'
else:
    new_word = string_input+'ing'

print(f'The newly formed word is : {new_word}')

# OUTPUT :

# Enter a word : happen
# The newly formed word is : happening

# Enter a word : awakening
# The newly formed word is : awakeningly
