# 5. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

num = input('Enter number whose factorial is to ba calculated : ')


def fact(factorial_of):
    factorial = 1

    for i in range(factorial_of, 1, -1):
        factorial *= i

    return factorial


print(f'{num}! = {fact(int(num))}')

# output

# Enter number whose factorial is to ba calculated : 5
# 5! = 120

