file = open("text.txt" , "r")
fil = file.read()
file.close()
count = 0
for word in fil:
    if word.isupper():
        count = count + 1
    else:
        count = count

print("The text is :", fil)
print("the number of uppercase:", count)