# 31. Write a Python program to iterate over dictionaries using for loops.


dictionary = {"name": "shreeti",
              "age": "24",
              "profession": "engineer",
              "address": "Kathmandu"
              }

for k in dictionary:
    print(f'{k} : {dictionary[k]}')
