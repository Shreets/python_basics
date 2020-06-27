# 13. Write a Python program to sort a list of tuples using Lambda.

family_age = [("Peter", 40), ("Stewie", 5), ("Meg", 16),
              ("Brian", 3), ("Lois", 38), ("Chris", 14)]
family_age.sort(key=lambda x: x[1])
print(f' The age of this family memer in order is as follows : \n{family_age}')

# OUTPUT

# The age of this family memer in order is as follows:
# [('Brian', 3), ('Stewie', 5), ('Chris', 14),
#  ('Meg', 16), ('Lois', 38), ('Peter', 40)]
