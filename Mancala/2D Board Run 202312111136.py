#%%
## IMPORT LIBRARY
import board as brd

thing = []
x_01 = []
x_02 = []
looper = 0
for a in (range(1, 100 + 1)):
    for b in (range(1, 100 + 1)):         
    
        ## VARIABLE INSTANTIATION
        board = brd.Board([a, b]) ## example of one that folds
        board_contents = board.get_board_contents()
        board_length = board.get_board_length()
        relative_board_indices = board.get_relative_board_indices()
        input_board_list = [board.get_board_contents()]
        input_board = board_contents.copy()
        output_board = board_contents.copy()
        contains_repeating_configurations = board.get_contains_repeating_configurations()
    
        ## ITERATIVE ONE-DIMENSION REDISTRIBUTION
        while contains_repeating_configurations == 0:
            board.distribute_dimensions(input_board, board, output_board, relative_board_indices, input_board_list)
            contains_repeating_configurations = board.get_contains_repeating_configurations()
            
        if len(input_board_list[-1]) == 1:
            contains_repeating_configurations = 0
        thing.append(contains_repeating_configurations)
        x_01.append(a)
        x_02.append(b)
        looper += 1
        print(looper)
