# 2. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.
# Sample String : 'Python'
# Expected Result : 'Pyon'
# Sample String : 'Py'
# Expected Result : 'PyPy'
# Sample String : ' w'
# Expected Result : Empty String


string_input = input('Enter any string : ')
str_length = len(string_input)
if str_length < 2:
    print('')

concat_string = string_input[0:2] + string_input[(str_length-2):(str_length)]

print(f'The fist two and last two results concatenated are : {concat_string}')

# OUTPUT:

# Enter any string : shreeti
# The fist two and last two results concatenated are : shti

# Enter any string : Us
# The fist two and last two results concatenated are : UsUs

# Enter any string : Six
# The fist two and last two results concatenated are : Siix
