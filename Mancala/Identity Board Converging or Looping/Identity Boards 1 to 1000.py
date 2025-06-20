#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 10:02:51 2025=

@author: rcole

PURPOSE:
    Part of Vignette 202506171745 - Identity Board Converging or Looping
    Looping through identity boards 1 to 1000 to see which ones / how many converge, and how many loop
"""

#%%


## IMPORT LIBRARIES
import board as brd
import pandas as pd 


#%%


## PARAMETERS
max_board_length = 1000


#%%


## LOOP THRU VARIOUS BOARDS
contains_repeating_configurations_list = []
trend_counter_list = []
contains_repeating_configurations = 0
for bl in range(1, max_board_length + 1):
    print(bl) #time check
    previous_contains_repeating_configurations = contains_repeating_configurations
    board = brd.Board([1] * bl) #create starting board
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
        
    ## APPENDING WHETHER CONFIG LOOPS
    contains_repeating_configurations_list.append(contains_repeating_configurations)
    
    ## APPENDING TO TREND COUNTER
    if bl == 1:
        trend_counter = 1
    elif contains_repeating_configurations == previous_contains_repeating_configurations:
        trend_counter = trend_counter + 1
    else:
        trend_counter = 1
    trend_counter_list.append(trend_counter)

#%%


## WRITE TO CSV
board_size = list(range(1, max_board_length + 1))
did_config_loop_df = pd.DataFrame({ 'board_size' : board_size, 'does_congifuration_loop' : contains_repeating_configurations_list, 'trend': trend_counter_list})
did_config_loop_df.to_csv(r'/Users/rcole/Desktop/imacgration/mcla/identity_board_converge_or_loop_0001_to_1000.csv', index = False)
