

#%%
## CLASS IDENTIFICATION


class Board:
    '''
    202311091716, rsc
    A board is a list consisting of numbers, tantamount to a mancala board.
    '''
    
    def __init__(self, boardContents):
        '''
        Create new Board instance
        '''
        self._boardContents = boardContents
        self._relativeBoardIndices = list(range(len(boardContents)))
        self._relativeBoardHistory = [boardContents].copy()
        self._turn = 0
        self._containsRepeatingConfigurations = 0
    def get_board_contents(self):
        '''
        Return Board contents
        '''
        return self._boardContents.copy()
    def get_board_length(self):
        '''
        Return Board length
        '''
        return len(self._boardContents)
    def get_relative_board_indices(self):
        '''
        Return relative Board indices
        '''
        return self._relativeBoardIndices
    def get_turn(self):
        '''
        Return the turn number
        '''
        return self._turn
    def get_contains_repeating_configurations(self):
        '''
        Return the no repeating configurations flag
        '''
        return self._containsRepeatingConfigurations
    def update_relative_board_history(self, newBoard):
        '''
        Update relative Board history with most recent relative board
        '''
        self._relativeHistory.append(newBoard)
    def update_turn(self):
        '''
        Update turn by incrementing 1
        '''
        self._turn += 1
    def update_contains_repeating_configurations(self, newValue):
        '''
        Update the contains repeating configurations flag
        '''
        self._containsRepeatingConfigurations = newValue
    def kenote_active_position(self, boardContents):
        '''
        Kenote, by which is meant "engage in an act of kenosis"
        Yes, it is a made-up word, as far as I know
        In any case, method sets value of specified position equal to 0
        '''
        boardContents[0] = 0
    def redistribute_first_position(self, input_board, output_board, gini, pareto):
        '''
        Redistribute the marbles in the first position to the other positions
        Return the what the new board looks like
        '''
        for e, i in enumerate(output_board):
            if pareto == 0:
                output_board[e] = input_board[e] + gini
            elif e == 0 or e > pareto:
                output_board[e] = input_board[e] + gini
            else:
                output_board[e] = input_board[e] + gini + 1
        return(output_board)
    def reset_relative_indices(self, activeSpot, boardLength, relativeBoardIndices):
        '''
        Reset relative indices
        Which is to say, return a list of where each spot is going to be in the next pecking order
        '''
        index_reset = 0
        leftovers = activeSpot % boardLength
        for i in range(leftovers, boardLength):
            relativeBoardIndices[i] = index_reset
            index_reset+=1
        for i in range(0, leftovers):
            relativeBoardIndices[i] = index_reset
            index_reset+=1
        return relativeBoardIndices
    def try_pop(self, list_to_check, value_to_check, list_to_pop):
        if 0 in input_board:
            value_to_pop = input_board.index(0)
        if value_to_check in list_to_check:
            list_to_pop.pop(value_to_pop)
        else:
            pass
        return list_to_pop
    def assemble_subsequent_input_board(self, output_board, input_board):
        '''
        Shuffle the elements of the board of a previous redistribution to render a board properly index for the next distribution
        Yes, the fact that our output board is essentially our input, and the input board is essentially our output, is something of a semantic souffle
        Oh well
        '''
        for e, i in enumerate(output_board):
            input_board[e] = output_board[relative_board_indices.index(e)]
        return(input_board)
    def distribute_dimensions(self, input_board, board, output_board, relative_board_indices, input_board_list):
        turn = board.get_turn()
        if turn > 0:
            output_board.pop(0)
            input_board.pop(input_board.index(0))
            relative_board_indices.pop(relative_board_indices.index(len(output_board)))
        board_length = len(output_board)
        spot_on_board_is_empty = 0
        contains_repeating_configurations = 0
        while spot_on_board_is_empty == 0 and contains_repeating_configurations == 0:
            first_position = input_board[0]
            gini = int((first_position - first_position % board_length) / board_length)
            pareto = first_position % board_length
            board.kenote_active_position(input_board)
            output_board = board.redistribute_first_position(input_board, output_board, gini, pareto)
            relative_board_indices = board.reset_relative_indices(first_position, board_length, relative_board_indices)
            input_board = board.assemble_subsequent_input_board(output_board, input_board)
            if (output_board.index(0) if 0 in output_board else -1) >= 0:
                spot_on_board_is_empty = 1
            if input_board in input_board_list:
                contains_repeating_configurations = 1
            else:
                input_board_list.append(input_board.copy())
        board.update_turn()
        board.update_contains_repeating_configurations(contains_repeating_configurations)

#%%
## VARIABLE INSTANTIATION


board = Board([9, 6, 4, 2]) ## example of one that cycles immediately  
#board = Board([14, 4, 8, 2]) ## example of one that folds
board_contents = board.get_board_contents()
board_length = board.get_board_length()
relative_board_indices = board.get_relative_board_indices()
input_board_list = [board.get_board_contents()]
input_board = board_contents.copy()
output_board = board_contents.copy()
contains_repeating_configurations = board.get_contains_repeating_configurations()


#%%
## ITERATIVE ONE-DIMENSION REDISTRIBUTION


while contains_repeating_configurations == 0:
    board.distribute_dimensions(input_board, board, output_board, relative_board_indices, input_board_list)
    contains_repeating_configurations = board.get_contains_repeating_configurations()

