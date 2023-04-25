# Open the file for reading
with open("data.txt", "r") as file:
    # Initialize variables for longest, shortest, and equal length words
    longest_word = ""
    shortest_word = ""
    equal_length_words = []

    # Loop through each line in the file
    for line in file:
        # Split the line into words
        words = line.split()
        # Loop through each word in the line
        for word in words:
            # Check if current word is longer than current longest word
            if len(word) > len(longest_word):
                longest_word = word
            # Check if current word is shorter than current shortest word
            if len(word) < len(shortest_word) or shortest_word == "":
                shortest_word = word
            # Check if current word has equal length with longest word
            if len(word) == len(shortest_word) and word :
                equal_length_words.append(word)

    # Print the longest word
    print("Longest word: ", longest_word)
    # Print the shortest word
    print("Shortest word: ", shortest_word)
    # Print any words with equal length with the longest word
    print("Words with equal length as longest word: ", ", ".join(equal_length_words))
