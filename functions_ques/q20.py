# 20. Write a Python program to find intersection of two given arrays using
# Lambda.


array1 = ['s', 'h', 'r', 'e', 'e', 't', 'i']
array2 = ['u', 'p', 'r', 'e', 't', 'i']


def intersect(array1, array2):
    common = list(filter(lambda x: x in array1, array2))
    print("Intersection of the two given arrays are is: ", common)


intersect(array1, array2)

# OUTPUT

# Intersection of the two given arrays are is:  ['r', 'e', 't', 'i']
