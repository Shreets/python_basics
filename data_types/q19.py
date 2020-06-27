
# 19. Write a Python program to get the smallest number from a list.

list_items = [16, 8, 71, -33, 12, 9, -14]

value = 0

for i in list_items:
    if i < value:
        value = i

print(f'The smallest value in the list is : {value}')
