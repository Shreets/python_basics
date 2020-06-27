
# 18. Write a Python program to get the largest number from a list.

list_items = [16, 8, 71, 33, 12, 9, 11]

value = 0

for i in list_items:
    if i > value:
        value = i

print(f'Thelargest value in the list is : {value}')
