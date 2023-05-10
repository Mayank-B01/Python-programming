def repeat_words(word):     # defining a function to check repeated words
    if len(word) == 0:      # setting base value to stop the function
        return {}
    current = word[0]       # checking the first word of the list
    freq = word.count(current)      # checking the occurrences of the same word
    remain = []         # initializing an empty list
    for words in word:  # using loop to count number of repetition
        if words != current:    # checking if the first element is same with the remaining word
            remain.append(words)       # adding the word in a list
    word_freq = {current: freq}        # creating a dictionary with the word and its occurrences
    remain_freq = repeat_words(remain)  # calling the function again for the remaining words
    for key, value in word_freq.items():    # checking the dictionary items
        remain_freq[key] = value            # adding / updating the dictionary
    return remain_freq


try:
    file = "temp.txt"               # storing file name in a variable
    with open(file, 'r') as file1:      # opening the file in read mode
        line = file1.readline()         # reading the contents of the file
        words = line.split(' ')         # separating the words in the file
    print("The words in the file are:", words)
    print(repeat_words(words))          # calling the function
except FileNotFoundError:               # exception handling for not finding the file
    print("file not found")
