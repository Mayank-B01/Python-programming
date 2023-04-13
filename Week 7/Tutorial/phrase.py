dic = {}
count = 1
found = True
file = open("phrase.txt", 'r')
f_line = file.readline().split(" ")
for letter in f_line:
    if letter in dic:
        dic[letter] = count + 1
        count = dic[letter]
    else:
        dic[letter] = count

print(dic)
