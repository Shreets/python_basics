# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.


string_input = input(
    'Enter words that you want in a list, SEPARATED by space : ')

word_list = string_input.split()

print(f'The list you have prepared is : {word_list}')

length = 0
word = ''

for i in word_list:
    if len(i) > length:
        length = len(i)
        word = i

print(f'The longest word in the list is {word} with length of {length}')


# OUTPUT

# Enter words that you want in a list, SEPARATED by space : javascript java python go

# The list you have prepared is : ['javascript', 'java', 'python', 'go']

# The longest word in the list is javascript with length of 10
