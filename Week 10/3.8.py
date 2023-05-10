def palindrome(word):       # defining a function
    if len(word) == 1:      # setting a base value
        return True
    if word[0] == word[-1]:     # checking if the first letter and the last letter are same
        remain = word[1:-1]     # taking all character except the first and last
        return palindrome(remain)   # using recursive function in the reaming characters
    else:
        return False


string = input("Enter the string:")         # asking for user input
print(palindrome(string))                   # calling the function
