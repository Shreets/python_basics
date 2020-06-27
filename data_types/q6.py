# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


string_input = input('Enter a sentence : ')

not_index = string_input.find('not')

poor_index = string_input.find('poor')


if (not_index != -1 and poor_index != -1) and not_index < poor_index:
    print(string_input.replace(
        string_input[not_index: (poor_index+4)], 'good'))
else:
    print(f'no changes in sentence due to no instnaces of poor followin not')

# OUTPUT

# Enter a sentence : i am not poor at maths
# i am good at maths
