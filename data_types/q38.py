# 38. Write a Python program to remove a key from a dictionary.

dic1 = {'a': 1, 'b': 2,  'c': 3, 'x': 4, 'y': 5, 'z': 6}

key_item = input('enter key you wanna delete : ')

del dic1[key_item]

print(dic1)

# OUTPUT

# enter key you wanna delete : x

# {'a': 1, 'b': 2, 'c': 3, 'y': 5, 'z': 6}
