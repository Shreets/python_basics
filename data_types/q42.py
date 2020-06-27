
# 42. Write a Python program to convert a list to a tuple.

tuple_list = ("javascript", "python", "django",
              "react", "sql", "git", "html", "css")

lists = list(tuple_list)

lists.append('go')

print(lists)

# OUTPUT
# ['javascript', 'python', 'django', 'react', 'sql', 'git', 'html', 'css', 'go']
