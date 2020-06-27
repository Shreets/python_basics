# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

string_input = input('Enter a string you wanna reverse : ')


def string_reverce(string_arg):
    string_list = list(string_arg)
    string_list.reverse()
    reversed_string = ""
    for i in string_list:
        reversed_string += i

    return reversed_string


print(string_reverce(string_input))

# OUTPUT
# Enter a string you wanna reverse : shreeti
# iteerhs
