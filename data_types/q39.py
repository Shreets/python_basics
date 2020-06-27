# 39. Write a Python program to unpack a tuple in several variables.


tuple_list = ("javascript", "python", "django",
              "react", "sql", "git", "html", "css")

a, b, c, d, *others = tuple_list

print(a)
print(b)
print(c)
print(d)
print(others)

# OUTPUT

# javascript
# python
# django
# react
# ['sql', 'git', 'html', 'css']
