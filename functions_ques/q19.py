# 19. Write a Python program to create Fibonacci series upto n using Lambda.


def fibobacci(n): return n if n <= 1 else fibobacci(n-1)+fibobacci(n-2)


for i in range(10):
    print(fibobacci(i))

# OUTPUT
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
