def initialise_board(board):
    """This function sets all the board elements to ' '-one space"""
    # develop code to set all elements of the board to one space ' '
    for i, element in enumerate(board):
        for j in range(len(element)):
            board[i][j] = ' '
    return board


def get_player_move(board):
    """This function asks the user where they want to input the cross in the matrix"""
    # develop code to ask the user for the cell to put the X in,
    print("""       
                       00 01 02
                       10 11 12        
    Choose your square:20 21 22 """)
    while True:
        row_choice = input("Enter row number:")           # asking user to input row value
        col_choice = input("Enter column number:")        # asking user to input column value
        if row_choice.isdigit() and col_choice.isdigit():  # checking if the input is a digit
            row = int(row_choice)
            col = int(col_choice)
            if 0 <= row <= 2:
                if 0 <= col <= 2:
                    if board[row][col] == ' ':
                        break
                    else:
                        print("Enter value for empty space")
                    continue
                else:
                    print("Enter correct column value")
                    continue
            else:
                print("Enter correct row  value.")
                continue
        else:
            print("Please enter numeric value")
    # and return row and col
    return row, col


result = initialise_board(board=[['1', '2', '3'],
                                 ['4', '5', '6'],
                                 ['7', '8', '9']])
get_player_move(result)
