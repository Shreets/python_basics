# 1. Write a Python function to find the Max of three numbers.


def compare_two(a, b):
    if a > b:
        return a
    return b


def compare_three(a, b, c):
    return compare_two(a, compare_two(b, c))


print(compare_three(21, 33, 14))
