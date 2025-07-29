
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 13:37:19 2025

@author: rcole
"""





import board as brd
import pandas as pd





board = brd.Board([1] * 52)
#board = brd.Board([50, 49, 49, 49, 49])
#board = brd.Board([1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2])
board_contents = board.get_board_contents()
board_length = board.get_board_length()
relative_board_indices = board.get_relative_board_indices()
input_board_list = [board.get_board_contents()]
input_board = board_contents.copy()
absolute_input_board = board_contents.copy()
output_board = board_contents.copy()
contains_repeating_configurations = board.get_contains_repeating_configurations()

absolute_index = 0
## ITERATIVE ONE-DIMENSION REDISTRIBUTION
while contains_repeating_configurations == 0:
    board.distribute_dimensions_with_minimal_energy(input_board, board, output_board, relative_board_indices, input_board_list, absolute_input_board, absolute_index)
    contains_repeating_configurations = board.get_contains_repeating_configurations()
    absolute_index = board.get_absolute_index()

    
if len(input_board_list[-1]) == 1:
    contains_repeating_configurations = 0

size = board.get_board_length()
mass = board.get_mass()
turns = board.get_turn()
total_energy = board.get_total_energy()
displaced_energy = board.get_displaced_energy()
    



