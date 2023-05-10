def draw_board(board):
    """This function is used to draw the board for the noughts and crosses games using - and |"""
    print('-------------')
    for rows in board:
        temp = '| '
        for elements in rows:
            temp += elements + ' | '
        print(temp)
        print('-------------')


draw_board(board=[['1', '2', '3'],
                  ['4', '5', '6'],
                  ['7', '8', '9']])
