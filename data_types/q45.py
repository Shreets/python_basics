
# 45. Write a Python program to find the index of an item of a tuple.

tuple_list = ("a", "s", "s", "i", "g", "n", "m", "e", "n", "t")
input_item = input("Enter the item whose index is to be found : ")
tuple_index = tuple_list.index(input_item)
print(f'The index of {input_item} is : {tuple_index}')

# OUTPUT

# Enter the item whose index is to be found : g

# The index of g is : 4
