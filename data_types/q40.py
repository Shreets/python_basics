# 40. Write a Python program to add an item in a tuple.

tuple_list = ("javascript", "python", "django",
              "react", "sql", "git", "html", "css")

lists = list(tuple_list)

lists.append('go')

tup_new = tuple(lists)

tup_new = tup_new + ("redux", "flask")

print(tup_new)

# OUTPUT
# ('javascript', 'python', 'django', 'react', 'sql', 'git', 'html', 'css', 'go','redux','flask')
