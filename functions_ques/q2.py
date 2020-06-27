
# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


list_items = [1, 3, 5, 7, 9, 11]


def sum_all(list_arg):
    total = 0
    for i in list_arg:
        total = total + i
    return total


print(sum_all(list_items))
