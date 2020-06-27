
# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.


def mul(number):
    return lambda x: x * number


multipication = mul(5)
print(f'the result to 5 multiplied by 18 is : {multipication(18)}')
