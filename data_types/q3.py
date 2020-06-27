# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


string_input = input('Enter a String : ')
first_word = string_input[0]

for i in string_input:
    if i == first_word.lower():
        new_string = first_word + string_input[1:].lower().replace(i, '$')

print(new_string)

# OUTPUT :
# Enter a String : Bamboozled_boB
# Bam$oozled_$o$
