# 18. Write a Python program to check whether a given string is number or not
# using Lambda.

def number(n): return True if n.isdigit() else False


print(f"Is  string 'ab123' a number? {number('ab123')}")


print(f"Is  string '12345' a number? {number('12345')}")


# output
# Is  string 'ab123' a number? False
# Is  string '12345' a number? True
