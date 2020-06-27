# 21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

list_item = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def last(n):
    return n[-1]


def sort_keys(tuples):
    return sorted(tuples, key=last)


print(sort_keys(list_item))
