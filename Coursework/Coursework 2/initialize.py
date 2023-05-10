def initialise_board(board):
    """This function sets all the board elements to ' '-one space"""
    # develop code to set all elements of the board to one space ' '
    for i, element in enumerate(board):
        for j in range(len(element)):
            board[i][j] = ' '
    return board


print(initialise_board(board=[['1', '2', '3'],
                              ['4', '5', '6'],
                              ['7', '8', '9']]))
