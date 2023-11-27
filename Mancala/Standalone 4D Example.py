

def reset_relative_indices(activeSpot, boardLength, relativeBoardIndices):
    index_reset = 0
    leftovers = activeSpot % boardLength
    for i in range(leftovers, boardLength):
        relativeBoardIndices[i] = index_reset
        index_reset+=1
    for i in range(0, leftovers):
        relativeBoardIndices[i] = index_reset
        index_reset+=1
    return relativeBoardIndices




board = [14, 4, 8, 2]
input_board = board.copy()
ouput_board = board.copy()
relative_board_indices = [0, 1, 2, 3]
board_length = len(board)




first_position = input_board[0]
gini = int((first_position - first_position % board_length) / board_length)
pareto = first_position % board_length
input_board[0] = 0
for e, i in enumerate(ouput_board):
    if pareto == 0:
        ouput_board[e] = input_board[e] + gini
    elif e == 0 or e > pareto:
        ouput_board[e] = input_board[e] + gini
    else:
        ouput_board[e] = input_board[e] + gini + 1
relative_board_indices = reset_relative_indices(first_position, board_length, relative_board_indices)
for e, i in enumerate(ouput_board):
    input_board[e] = ouput_board[relative_board_indices.index(e)]
    



first_position = input_board[0]
gini = int((first_position - first_position % board_length) / board_length)
pareto = first_position % board_length
input_board[0] = 0
for e, i in enumerate(ouput_board):
    if pareto == 0:
        ouput_board[e] = input_board[e] + gini
    elif e == 0 or e > pareto:
        ouput_board[e] = input_board[e] + gini
    else:
        ouput_board[e] = input_board[e] + gini + 1
relative_board_indices = reset_relative_indices(first_position, board_length, relative_board_indices)
for e, i in enumerate(ouput_board):
    input_board[e] = ouput_board[relative_board_indices.index(e)]




first_position = input_board[0]
gini = int((first_position - first_position % board_length) / board_length)
pareto = first_position % board_length
input_board[0] = 0
for e, i in enumerate(ouput_board):
    if pareto == 0:
        ouput_board[e] = input_board[e] + gini
    elif e == 0 or e > pareto:
        ouput_board[e] = input_board[e] + gini
    else:
        ouput_board[e] = input_board[e] + gini + 1
relative_board_indices = reset_relative_indices(first_position, board_length, relative_board_indices)
for e, i in enumerate(ouput_board):
    input_board[e] = ouput_board[relative_board_indices.index(e)]

