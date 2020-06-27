# 28. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dictionary = {0: 10, 1: 20}

key_input = input('enter key value : ')
value_input = input('enter value : ')

dictionary.update({key_input: value_input})

print(dictionary)

# OUTPUT
# enter key value : 5
# enter value : 66
# {0: 10, 1: 20, '5': '66'}
