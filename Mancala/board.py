#%%
## CLASS IDENTIFICATION
import math


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
        self._turn = 0
        self._containsRepeatingConfigurations = 0
        self._mass = 0
        self._totalEnergy = 0
        self._displacedEnergy = 0
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
        Return the contains repeating configurations flag
        '''
        return self._containsRepeatingConfigurations
    def get_mass(self):
        '''
        Return the Mass
        '''
        return self._mass
    def get_total_energy(self):
        '''
        Return the Total Energy quantity
        '''
        return self._totalEnergy
    def get_displaced_energy(self):
        '''
        Return the Displaced Energy quantity
        '''
        return self._displacedEnergy
    def update_turn(self):
        '''
        Update turn by incrementing 1
        '''
        self._turn += 1
    def update_mass(self, newValue):
        '''
        Update turn by incrementing 1
        '''
        self._mass = newValue
    def update_contains_repeating_configurations(self, newValue):
        '''
        Update the contains repeating configurations flag
        '''
        self._containsRepeatingConfigurations = newValue
    def update_total_energy(self, addedAmount):
        '''
        Update the Total Energy quantity
        '''
        self._totalEnergy = self._totalEnergy + addedAmount
    def update_displaced_energy(self, addedAmount):
        '''
        Update the Displaced Energy quantity
        '''
        self._displacedEnergy = self._displacedEnergy + addedAmount
    def find_min_exponent(self, a, b, threshold):
        value_is_too_small = 1
        current_value = a * b
        exponent = 1
        return_value = 0
        return_object = []
        while value_is_too_small == 1:
            current_value = current_value * b 
            if current_value > threshold:
                value_is_too_small = 0
                return_value = current_value
            exponent = exponent + 1
            return_object = [exponent, return_value]
        return(return_object) 
    def hitch_ride(self, active_position, board_length):
        coefficient_list = []
        min_exponent_list = []
        value_list = []
        for coefficient in range(1, board_length):
            min_exponent_object = self.find_min_exponent(coefficient, board_length, active_position)
            min_exponent = min_exponent_object[0]
            value = min_exponent_object[1]
            coefficient_list.append(coefficient)
            min_exponent_list.append(min_exponent)
            value_list.append(value)
        smallest_value = min(value_list)
        smallest_value_index = value_list.index(smallest_value)
        optimal_exponent = min_exponent_list[smallest_value_index]
        opitmal_coefficient = coefficient_list[smallest_value_index]
        return(smallest_value) 
    def consecutive_distributions_succeed(self, active_position, board_length):
        number_still_an_integer = 1
        while number_still_an_integer == 1:
            new_number = active_position / board_length 
            if new_number.is_integer():
                active_position = new_number
            else:
                number_still_an_integer = 0
        if active_position <= board_length:
            bin_consecutive_distributions_succeed = 1
        else:
            bin_consecutive_distributions_succeed = 0
        return(bin_consecutive_distributions_succeed)
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
    def assemble_subsequent_input_board(self, output_board, input_board, relative_board_indices):
        '''
        Shuffle the elements of the board of a previous redistribution to render a board properly index for the next distribution
        Yes, the fact that our output board is essentially our input, and the input board is essentially our output, is something of a semantic souffle
        Oh well
        '''
        for e, i in enumerate(output_board):
            input_board[e] = output_board[relative_board_indices.index(e)]
        return(input_board)
    def distribute_dimensions(self, input_board, board, output_board, relative_board_indices, input_board_list):
        '''
        Wrapper for omnibus method that contains other methods (including redistribute_first_position, reset_relative_indices, assemble_subsequent_input_board)
        These methods do bulk of the work, including redistributing marbles, resetting indices, and assembling subsequent input board
        This should probably be broken up at some point into additional methods
        '''
        turn = board.get_turn()
        ## slightly special rule needed for first distribution
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
            input_board = board.assemble_subsequent_input_board(output_board, input_board, relative_board_indices)
            if (output_board.index(0) if 0 in output_board else -1) >= 0:
                spot_on_board_is_empty = 1
            if input_board in input_board_list:
                contains_repeating_configurations = 1
            else:
                input_board_list.append(input_board.copy())
        board.update_turn()
        board.update_contains_repeating_configurations(contains_repeating_configurations)
    def distribute_dimensions_with_minimal_energy(self, input_board, board, output_board, relative_board_indices, input_board_list):
        '''
        Wrapper for omnibus method that contains other methods (including redistribute_first_position, reset_relative_indices, assemble_subsequent_input_board)
        These methods do bulk of the work, including redistributing marbles, resetting indices, and assembling subsequent input board
        This should probably be broken up at some point into additional methods
        '''
        turn = board.get_turn()
        ## slightly special rule needed for first distribution
        
        if turn > 0:
            output_board.pop(0)
            input_board.pop(input_board.index(0))
            relative_board_indices.pop(relative_board_indices.index(len(output_board)))
        board_length = len(output_board)
        spot_on_board_is_empty = 0
        contains_repeating_configurations = 0
        while spot_on_board_is_empty == 0 and contains_repeating_configurations == 0:
            first_position = input_board[0]
            ## small number, big board --> distribute
            ## ex [2, 2, 2, 2, 2]
            if first_position <= board_length: 
                first_position = first_position
                #print('a')
            ## active position is a power of board length --> distribute
            ## ex [125, 124, 124, 124, 124]
            elif board_length > 1 and math.log(first_position, board_length).is_integer():
                first_position = first_position
                #print('b')
            ## several power downs of first position lead to small number --> distribute
            ## ex [250, 2, 2, 2, 2]
            elif board_length > 1 and self.consecutive_distributions_succeed(first_position, board_length) == 1:
                first_position = first_position
                #print('c')
            ## active position is multiple of big board, and remainder is small
            ## ex [8, 8, 7, 7]
            elif first_position % board_length == 0 and first_position / board_length <= board_length:
                first_position = first_position
                #print('d')
            ## slight add-on can get active position to spin once into a smaller numper
            elif (first_position + board_length - (first_position % board_length)) / board_length <= board_length:
                first_position = (first_position + board_length - (first_position % board_length))
                #print('e')
            elif board_length > 1:
                first_position = self.hitch_ride(first_position, board_length) 
                #print('f')
            else:
                first_position = first_position
                #print('g')
            gini = int((first_position - first_position % board_length) / board_length)
            pareto = first_position % board_length
            board.kenote_active_position(input_board)
            output_board = board.redistribute_first_position(input_board, output_board, gini, pareto)
            relative_board_indices = board.reset_relative_indices(first_position, board_length, relative_board_indices)
            input_board = board.assemble_subsequent_input_board(output_board, input_board, relative_board_indices)
            if (output_board.index(0) if 0 in output_board else -1) >= 0:
                spot_on_board_is_empty = 1
            if input_board in input_board_list:
                contains_repeating_configurations = 1
            else:
                input_board_list.append(input_board.copy())
            if contains_repeating_configurations != 1 and len(input_board) > 1:
                board.update_total_energy(first_position)
                board.update_displaced_energy(first_position - gini)
            if contains_repeating_configurations != 1:
                board.update_turn()
        board.update_contains_repeating_configurations(contains_repeating_configurations)
        board.update_mass(sum(input_board))
        
