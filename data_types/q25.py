# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

list_items_1 = [{}, {}, {}]
list_items_2 = [{1, 2}, {}, {}]
is_empty_1 = all(len(d) == 0 for d in list_items_1)
is_empty_2 = all(len(d) == 0 for d in list_items_2)

if is_empty_1:
    print(f'list_items_1 is empty : {list_items_1}')
if is_empty_2:
    print(f'list_items_2 is empty : {list_items_2}')
else:
    ('none of these are empty')
