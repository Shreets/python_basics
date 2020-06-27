# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

list_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def even(list_arg):
    even_list = []

    for i in list_arg:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


print(f' even items list : {even(list_items)}')


# output
# even items list : [2, 4, 6, 8]
