#!/usr/bin/python3

'''Defines the logic behind switching play between players on the board'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple as NT
from tic_tac_toe_player import Player
from tic_tac_toe_move import Move
from tic_tac_toe_game import Game
from tic_tac_toe_game import board_setup
from tic_tac_toe_game import get_name
from valid_move import is_move_valid
from get_winning import get_winning_combination
from processing_move import process_move
from is_winner import any_winner
from game_tied import is_tied


def switch_player(self):
    '''Returns the switched player'''
    self.current_player = next(self.players)
