def draw_board(board):
    """This function is used to draw the board for the noughts and crosses games using - and |"""
    print('-------------')
    for rows in board:
        temp = '| '
        for markers in rows:
            temp += markers + ' | '
        print(temp)
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


welcome(board=[['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9']])
