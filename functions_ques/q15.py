# 15. Write a Python program to filter a list of integers using Lambda.


num = [21, 12, 34, 43, 15, 61, 77, 81, 49]

even = list(filter(lambda x: x % 2 == 0, num))
odd = list(filter(lambda x: x % 2 != 0, num))

print(f"filtered even list :{even}")
print(f"filtered even list :{odd}")
