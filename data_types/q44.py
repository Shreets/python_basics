# 44. Write a Python program to slice a tuple.

tuple_list = ("a", "s", "s", "i", "g", "n", "m", "e", "n", "t")

slice1 = tuple_list[:6]

slice2 = tuple_list[::2]

slice3 = tuple_list[::-1]

print(slice1)

# ('a', 's', 's', 'i', 'g', 'n')

print(slice2)
# ('a', 's', 'g', 'm', 'n')

print(slice3)
# ('t', 'n', 'e', 'm', 'n', 'g', 'i', 's', 's', 'a')

# OUTPUT
