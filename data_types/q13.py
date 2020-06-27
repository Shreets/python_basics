# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red


string_input = input('Enter words separated by comma : \n')

list_string = string_input.split(',')

list_string.sort()

final_word = list_string[0]

for i in list_string[1:]:
    final_word = final_word + ' , ' + i

print(final_word)

# #OUTPUT
# Enter words separated by comma :
# a,s,d,f,g,h,j,l

# a , d , f , g , h , j , l , s
