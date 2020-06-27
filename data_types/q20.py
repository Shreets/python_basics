# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

list_item = ['ABBA', 'absolute', 'chronic',
             'dread', 'python', 'be', 'dad', 'xx']
new_list = []
for i in list_item:
    if len(i) >= 2 and i[0] == i[-1]:
        new_list.append(i)


print(
    f'the number of worst starting and ending with same letters are {len(new_list)} and this words are : \n{new_list}')

# OUTPUT

# the number of worst starting and ending with same letters are 5 and this words are :
# ['ABBA', 'chronic', 'dread', 'dad', 'xx']
