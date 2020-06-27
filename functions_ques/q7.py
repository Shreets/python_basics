# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


string_input = input('Enter a number sentence : ')


def case_check(string_arg):
    upper = 0
    lower = 0

    for i in string_arg.replace(" ", ""):
        if i.islower():
            lower = lower+1
        else:
            upper = upper+1

    return {'upper': upper, 'lower': lower}


case_dict = case_check(string_input)
# print(case_dict['upper'])
print(f"Total number of uppercase letters : {case_dict['upper']}")
print(f"Total number of lowercase letters : {case_dict['lower']}")

# OUTPUT

# Enter a number sentence : PyThOn AsSiGnMeNt
# Total number of uppercase letters : 8
# Total number of lowercase letters : 8
