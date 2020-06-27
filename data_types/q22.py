# 22. Write a Python program to remove duplicates from a list.


list_items = [0, 0, 13, 21, 34, 56, 13, 13, 12, 11, 34]

new_list = []

for i in list_items:
    if i not in new_list:
        new_list.append(i)

# Alternative one-liner for this
# new_list = set(list_items)

print(f'the list with removed duplicates is as given : \n {new_list}')
