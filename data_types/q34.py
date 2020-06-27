# 34. Write a Python script to merge two Python dictionaries.

dic1 = {'a': 100, 'b': 200,  'c': 200}
dic2 = {'x': 400, 'y': 500, 'z': 500}

dic1.update(dic2)

print(f'The merges result is : {dic1}')

# OUTPUT

# The merges result is : {'a': 100, 'b': 200, 'c': 200, 'x': 400, 'y': 500, 'z': 500}
