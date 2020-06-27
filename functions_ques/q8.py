# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


list_items = [1, 2, 3, 3, 3, 3, 4, 5]


def unique_list(list_arg):
    unq_list = []

    for i in list_arg:
        if i not in unq_list:
            unq_list.append(i)
    return(unq_list)


print(f' unique list : {unique_list(list_items)}')
