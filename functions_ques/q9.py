# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.

num = input('enter a number to check if it is prime : ')


def check_prime(number):
    count = 0
    if number == 1:
        print(f'The number {number} is not prime')
    elif number == 2:
        print(f'The number {number} is not prime')
    else:
        for i in range(2, number):
            if number % i == 0:
                count = count+1

    if count >= 1:
        print(f'The number {number} is not prime')
    else:
        print(f'The number {number} is prime')


check_prime(int(num))

# OUTPUT
# enter a number to check if it is prime : 9
# The number 9 is not prime
