import random
import draw_board


def choose_computer(board):
    new_lst = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                new_lst.append([i,j])
    position = random.choice(new_lst)  # choosing an empty places
    row = position[0]               # taking first value as row
    col = position[1]
    return row, col


choose_computer(draw_board)