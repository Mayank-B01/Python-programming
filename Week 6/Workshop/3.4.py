# creating a string set
set_strng = {"USA", "Nepal", "India", "China", "Oman"}
# creating an empty set
new_lst = set()
# checking the first letter of each element
for letter in set_strng:
    if letter[0].lower() == 'a' or letter[0].lower() == 'e' or letter[0].lower() == 'i' or letter[0].lower() == 'o' or letter[0].lower() == 'u':
        new_lst.add(letter)
# printing new set with initial vowel alphabet
print(new_lst)
