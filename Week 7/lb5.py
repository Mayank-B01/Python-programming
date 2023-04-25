with open("data.txt") as file:
    fil = file.read()
    equal_word = []
    highest = ''
    shortest = ''
    line = fil.split()
    for word in line:
        if len(word) > len(highest):
            highest = word
        if len(word) < len(shortest) or shortest =='':
            shortest = word
        if len(word) == len(highest) and word not in equal_word:
            equal_word.append(word)

print('longest=', highest, '\n')
print('sortest=', shortest, '\n')
if equal_word:
    print(",".join(equal_word))
