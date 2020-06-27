# 14. Write a Python program to sort a list of dictionaries using Lambda.


family_age = [{'name': 'Peter', 'age': 40}, {'name': 'Stewie', 'age': 5}, {
    'name': 'Meg', 'age': 15}, {'name': 'Brian', 'age': 3}, {'name': 'louis', 'age': 35}]

sorted_list = sorted(family_age, key=lambda k: k['name'])
print(
    f' The age of this family memer in order is as follows : \n{sorted_list}')

# # OUTPUT
# The age of this family memer in order is as follows:
# [{'name': 'Brian', 'age': 3}, {'name': 'Meg', 'age': 15}, {'name': 'Peter','age': 40}, {'name': 'Stewie', 'age': 5}, {'name': 'louis',age': 35}]
