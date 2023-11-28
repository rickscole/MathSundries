

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
output_board = board.copy()
relative_board_indices = [0, 1, 2, 3]
board_length = len(board)



spot_on_board_is_empty = 0
while spot_on_board_is_empty == 0:
    first_position = input_board[0]
    gini = int((first_position - first_position % board_length) / board_length)
    pareto = first_position % board_length
    input_board[0] = 0
    for e, i in enumerate(output_board):
        if pareto == 0:
            output_board[e] = input_board[e] + gini
        elif e == 0 or e > pareto:
            output_board[e] = input_board[e] + gini
        else:
            output_board[e] = input_board[e] + gini + 1
    relative_board_indices = reset_relative_indices(first_position, board_length, relative_board_indices)
    for e, i in enumerate(output_board):
        input_board[e] = output_board[relative_board_indices.index(e)]
    if (output_board.index(0) if 0 in output_board else -1) >= 0:
        spot_on_board_is_empty = 1
    print(input_board)



