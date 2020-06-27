# 43. Write a Python program to remove an item from a tuple.

tuple_list = ("a", "s", "s", "i", "g", "n", "m", "e", "n", "t")
input_item = input('Enter item you wanna remove : ')
lists = list(tuple_list)

lists.remove(input_item)

new_tuple = tuple(lists)
print(f'new tuple list : {new_tuple}')

# OUTPUT

# Enter item you wanna remove : g

# new tuple list : ('a', 's', 's', 'i', 'n', 'm', 'e', 'n', 't')
