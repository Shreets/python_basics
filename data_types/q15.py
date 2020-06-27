# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


def insert_sting_middle(middle_of, middle_content):
    middle_index = int(int(len(middle_of))/2)
    new_content = middle_of[:middle_index] + \
        middle_content+middle_of[middle_index:]
    return new_content


print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<<>>>', 'JS'))
print(insert_sting_middle('||||||||', 'React'))

# OUTPUT

# [[Python]]
# {{PHP}}
# <<<JS>>>
# ||||React||||
