#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 10:41:46 2025

@author: rcole
"""




import board as brd
import pandas as pd


size_list = []
mass_list = []
turns_list = []
total_energy_list = []
displaced_energy_list = []
input_board_fold_list = []

for i in range(1, 1200 + 1):
    print(i)
    board = brd.Board([1] * i)
    #board = brd.Board([1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2])
    board_contents = board.get_board_contents()
    board_length = board.get_board_length()
    relative_board_indices = board.get_relative_board_indices()
    input_board_list = [board.get_board_contents()]
    input_board = board_contents.copy()
    output_board = board_contents.copy()
    contains_repeating_configurations = board.get_contains_repeating_configurations()
    
    ## ITERATIVE ONE-DIMENSION REDISTRIBUTION
    while contains_repeating_configurations == 0:
        board.distribute_dimensions_with_minimal_energy(input_board, board, output_board, relative_board_indices, input_board_list)
        contains_repeating_configurations = board.get_contains_repeating_configurations()
        
    if len(input_board_list[-1]) == 1:
        contains_repeating_configurations = 0
    
    size = board.get_board_length()
    mass = board.get_mass()
    turns = board.get_turn()
    total_energy = board.get_total_energy()
    displaced_energy = board.get_displaced_energy()
    input_board_fold = [input_board_list]
    
    size_list.append(size)
    mass_list.append(mass)
    turns_list.append(turns)
    total_energy_list.append(total_energy)
    displaced_energy_list.append(displaced_energy)
    #input_board_fold_list.append(input_board_fold)


df = pd.DataFrame({'size' : size_list, 'mass' : mass_list, 'turns' : turns_list
                   , 'total energy' : total_energy_list, 'displaced energy' : displaced_energy_list
                   })
df.to_csv(r'/Users/rcole/Desktop/imacgration/mcla/minimal energy configs 1 to 1200.csv', index = False)
