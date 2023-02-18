#!/usr/bin/python3

'''Defines the Move class'''
import tkinter as kin
from itertools import cycle
from tkinter import font
from typing import NamedTuple
from player import Player


class Move(NamedTuple):
    '''Move class that inherited NamedTuple class of typing module'''
    row: int
    col: int
    label: str = ""


BOARD_SIZE = 4
DEFAULT_PLAYERS = (
    Player(label="UD", color="purple"),
    Player(label="JEK", color="orange"),
)
