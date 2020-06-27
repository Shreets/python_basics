# 6. Write a Python function to check whether a number is in a given range.

upper_limit = 75
lower_limit = 20

num = input('Enter a number you wanna check : ')


def range_check(ceil, floor, number):
    if floor < number < ceil:
        print(f'{number} is withing the range of {floor} and {ceil}')
    elif floor > number:
        print(f'{number} is below the range of {floor} and {ceil}')
    else:
        print(f'{number} is above the range of {floor} and {ceil}')


range_check(upper_limit, lower_limit, int(num))

# OUTPUT
# Enter a number you wanna check : 36
# 36 is withing the range of 20 and 75
