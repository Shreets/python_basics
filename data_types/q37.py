# 37. Write a Python program to multiply all the items in a dictionary.

dic1 = {'a': 1, 'b': 2,  'c': 3, 'x': 4, 'y': 5, 'z': 6}

mul = 1

for k in dic1:
    mul = mul*dic1[k]

print(f'the multipication result of all items is : {mul}')
