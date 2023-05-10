import random
import json
from os.path import exists
random.seed()


def draw_board(board):
    """This function is used to draw the board for the noughts and crosses games using - and |"""
    print('-------------')
    for rows in board:  # used to access every row in the board
        pipe = '| '  # initializing a pipe to insert between the input
        for elements in rows:  # loop to insert the pipe between the possible inputs
            pipe = pipe + elements + ' | '
        print(pipe)
        print('-------------')


def welcome(board):
    """This function is used to display the welcome message along with the structure of the board"""
    # prints the welcome message
    print('''
Welcome to the "Unbeatable Noughts and Crosses" game.
The board layout is shown below:''')
    # display the board by calling draw_board(board)
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want ")


def initialise_board(board):
    """This function sets all the board elements to ' '-one space"""
    # develop code to set all elements of the board to one space ' '
    for i, element in enumerate(board):  # differentiating out the index and object of each row
        for j in range(len(element)):  # working on the markers / elements of each row
            board[i][j] = ' '  # replacing the displayed elements with blank space
    return board


def get_player_move(board):
    """This function asks the user where they want to input the cross in the matrix"""
    # develop code to ask the user for the cell to put the X in,
    print("""       
                       00 01 02
                       10 11 12        
    Choose your square:20 21 22 """)
    row_choice, col_choice = '', ''
    while True:
        row_choice = input("Enter row number:")  # asking user to input row value
        if not row_choice.isdigit():  # checking for non-numeric inputs
            print('Invalid input. Enter a number.')
            continue
        if not 0 <= int(row_choice) < 3:  # checking if number is within range
            print('Invalid input. Please type a number between (0-2)')
            continue
        while True:
            col_choice = input('Enter column: ')
            if not col_choice.isdigit():  # checking if input is digit
                print('Invalid input. Enter a number.')
                continue
            if not 0 <= int(col_choice) < 3:    # checking the range of input
                print('Invalid input. Please type a number between (0-2)')
            else:
                break
        break
    row = int(row_choice)       # converting into integer for processing
    col = int(col_choice)
    position = board[row][col]
    if not position == ' ':  # checks if user's choice is empty or not
        print('Please choose empty space')
        return None, None
    return row, col


def choose_computer_move(board):
    """This function searches for the empty spaces in the matrix and
    generates random position according to it for nought to be placed as the
    computer input."""
    # develop code to let the computer chose a cell to put a nought in
    spaces = []
    length = len(board)
    for i in range(length):  # searching columns of the matrix
        for j in range(length):  # searching rows of the matrix
            if board[i][j] == ' ':
                spaces.append([i, j])  # making list of empty spaces
    position = random.choice(spaces)  # choosing an empty places
    row = position[0]  # taking first value as row
    col = position[1]  # taking second value as column
    # and return row and col
    return row, col


def check_for_win(board, mark):
    """This function checks the board if the user or the computer has won
    and returns True when someone has won."""
    # develop code to check if either the player or the computer has won
    length = len(board)
    for i in range(length):  # loop for checking the rows
        row_full, col_full = True, True
        for j in range(length):  # checking the choices of the user and computer
            if board[i][j] != mark:  # checking rows if they are same
                row_full = False
            if board[j][i] != mark:  # checking column if they are same
                col_full = False
        if row_full or col_full:  # checking if either row or column is full
            return True
    left_diagonal, right_diagonal = True, True
    for i in range(length):
        if board[i][i] != mark:  # checking the left diagonal
            left_diagonal = False
        if board[i][length - i - 1] != mark:  # checking the right diagonal
            right_diagonal = False
    if left_diagonal or right_diagonal:  # checking if either left or right diagonal is full
        return True
    return False


def check_for_draw(board):
    """This function checks every element in the board for draw scenario"""
    # develop cope to check if all cells are occupied
    for element in board:  # checking every element in the board
        if ' ' in element:  # looking for empty space
            return False  # returning False if there is empty space
    # return True if all space occupied
    return True


def play_game(board):
    """This function allows the user to play the game"""
    # star with a call to the initialise_board(board) function to set
    player_input = False
    match_status = True
    board = initialise_board(board)
    welcome(board)
    # then in a loop, get the player move, update and draw the board
    while match_status:  # creating a loop to fill the board
        while not player_input:
            player_row, player_column = get_player_move(board)  # taking user input by calling get_player_move function
            if (player_row, player_column) == (None, None):  # checking for empty input by the user
                print("The entered row and column is not empty")
                continue
            board[player_row][player_column] = 'X'  # assigning 'X' to user input position
            draw_board(board)  # displaying user's move
            break
        # checking if the player has won by calling check_for_win(board, mark),
        if check_for_win(board, "X"):
            print("You won!!")
            return 1  # returning score of 1 when the user wins
        if check_for_draw(board):  # checking for draw
            print("The match is drawn.")
            return 0
        computer_row, computer_column = choose_computer_move(board)  # taking computer move position
        board[computer_row][computer_column] = "O"  # assigning 'O' for computer choice in board
        print("Computer choice is:")
        draw_board(board)  # displaying computer's move
        if check_for_win(board, "O"):  # checking if the computer has won
            print("You Lost!! Computer won.")
            draw_board(board)
            return -1
        if check_for_draw(board):  # checking for draw
            print("The match is drawn.")
            draw_board(board)
            return 0


def menu():
    """This function displays the menu for the game and
    prompts the user to enter 1-play game, 2-save game, 3-load the leaderboard
    and 4-quit the game and call functions accordingly."""
    while True:
        user_input = input('''                 
Enter one of the following options:
        1 - Play the game
        2 - Save your score in the leaderboard
        3 - Load and Display the Leaderboard
        q - End the program
1, 2, 3, or q? ''')  # displaying the menu and prompting the user to input 1, 2, 3, or q
        if user_input.lower() in ["1", "2", "3", "q"]:  # checking user input
            return user_input.lower()
        print("Your input is invalid! Try again")


def load_scores():
    """This function loads the leaderboard stored in 'leaderboard.txt' file"""
    # develop code to load the leaderboard scores
    leaders = {}  # creating an empty dictionary
    if not exists('leaderboard.txt'):  # checking if the file for leaderboard exists
        print("File does not exists. Creating new file.")
        with open('leaderboard.txt', 'w') as file:
            json.dump({}, file)                      # using json to write in the file
    with open("leaderboard.txt", 'r') as r_file:  # opening the file if its exists in read mode
        line = r_file.read()  # reading the data in the file
    try:
        leaders = json.loads(line)  # loading the read lines in the dictionary
    except json.JSONDecodeError:  # error handling
        with open('leaderboard.txt', 'w') as main_file:  # opening a file when the error occurs
            json.dump({}, main_file)  # loading the data of the file in the dictionary
    return leaders  # returning the dictionary


def save_score(score):
    """This function helps to save the score of the user in the 'leaderboard.txt file
    creating a leaderboard by asking user's name."""
    # develop code to ask the player for their name
    name = input("Enter your name:")  # asking user to input name
    current_leader = load_scores()  # calling current leaderboard
    players = current_leader.keys()  # calling current players
    if name in players:  # searching if name exists previously
        old_score = current_leader[name]  # checking old score
        new_score = old_score + score  # adding new score
        current_leader[name] = new_score  # updating the score
    else:
        current_leader[name] = score
    with open("leaderboard.txt", "w") as file:  # opening the file in write mode
        json.dump(current_leader, file)  # writing the updated / new score in the file
        print("Leaderboard updated")


def display_leaderboard(leaders):
    """This function displays the overall leaderboard"""
    print('''Noughts and Crosses Leaderboard ''')
    if leaders == {}:  # checking if the dictionary is empty
        print("No players currently.")
    else:
        for players, score in leaders.items():  # accessing the player names and their score
            print(players, "has score of ", score)
