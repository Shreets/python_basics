# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda.


num_list = [1, 2, 3, 4, 5]


def square(number):
    return list(map(lambda x: x ** 2, num_list))


def cube(number):
    return list(map(lambda x: x ** 3, num_list))


print(f'the square value is : {square(num_list)}')
print(f'the cube value is : {cube(num_list)}')


# OUTPUT

# the square value is : [1, 4, 9, 16, 25]
# the cube value is : [1, 8, 27, 64, 125]
