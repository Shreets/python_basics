# 12. Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.


string_input = input("Enter a string : ")

print(f'The sentence in all lowercase : /n {string_input.lower()}')

print('##########################################################')

print(f'The sentence in all Upper case : /n {string_input.upper()}')

print('##########################################################')

print(
    f'The sentence in all capitalized first letter  : /n {string_input.capitalize()}')

# OUTPUT

# Enter a string : This is the 12th question in this assignment

# The sentence in all lowercase : /n this is the 12th question in this assignment

# ##########################################################

# The sentence in all Upper case : /n THIS IS THE 12TH QUESTION IN THIS ASSIGNMENT
