
# 36. Write a Python program to sum all the items in a dictionary.


dic1 = {'a': 100, 'b': 200,  'c': 200, 'x': 400, 'y': 500, 'z': 600}

sum = 0

for k in dic1:
    sum = sum+dic1[k]

print(f'the sume of all items is : {sum}')
