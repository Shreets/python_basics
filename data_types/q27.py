# 27. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

first_list = [1, 3, 5, 7, 9, 10]
second_list = [2, 4, 6, 8]


first_list[-1:] = second_list

print(first_list)
