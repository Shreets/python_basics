# 17. Write a Python program to find if a given string starts with a given character
# using Lambda.

def start(word): return True if word.startswith('S') else False


print(f"Does word Assignment starts with given string ? {start('Assignment')}")


print(f"Does word Shreeti starts with given string ? {start('Shreeti')}")


# output
# Does word Assignment starts with given string ? False
# Does word Shreeti starts with given string ? True
