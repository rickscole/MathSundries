#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 10:44:13 2025

@author: rcole
"""

import board as brd


board = brd.Board([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
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
