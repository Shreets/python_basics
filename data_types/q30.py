# 30. Write a Python script to check whether a given key already exists in a
# dictionary.

dictionary = {"name": "shreeti",
              "age": "24",
              "profession": "engineer"}

key_input = input('Enter the key you want to check in dictionary : ')

if key_input in dictionary.keys():
    print(f"The key '{key_input}' exists")
else:
    print(f"The key '{key_input}' doesnt exist")
