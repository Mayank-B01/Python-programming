# asking a user to input a string
word = input("Enter any string value:")
# creating a variable to store reverse string
rev_word = ''
# creating a loop to reverse the string
for i in range(len(word)):
    rev_word = word[i] + rev_word

print(rev_word)
    
