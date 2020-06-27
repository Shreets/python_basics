# 32. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dictionary = dict()

nth_value = input('enter the nth value : ')

for i in range(1, int(nth_value)+1):
    dictionary[i] = i*i

print(dictionary)

# OUTPUT

# enter the nth value : 8

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
