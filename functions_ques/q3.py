

# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

list_items = [1, 3, 5, 7, 9, 11, -5]


def mul_all(list_arg):
    mul = 1
    for i in list_arg:
        mul = mul * i
    return mul


print(mul_all(list_items))
