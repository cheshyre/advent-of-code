# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib
import re

DIRS = ["^", ">", "v", "<"]
DIRS_COORDS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

input_lines = get_input_lines()


def add_pos(pos, inc):
    return pos[0] + inc[0], pos[1] + inc[1]


def is_pos_within_bounds(board, pos):
    if pos[0] < 0 or pos[1] < 0:
        return False
    if pos[0] >= len(board) or pos[1] >= len(board[0]):
        return False

    return True


def get_val_at_pos(board, pos):
    return board[pos[0]][pos[1]]


def set_val_at_pos(board, pos, val):
    board[pos[0]][pos[1]] = val
    return board


def simulate_step(board, pos, dir):
    new_pos = add_pos(pos, DIRS_COORDS[dir])
    if is_pos_within_bounds(board, new_pos) and get_val_at_pos(board, new_pos) == "#":
        new_dir = DIRS[
            (DIRS.index(dir) + 1) % len(DIRS)
        ]
        return board, pos, new_dir
    return board, new_pos, dir


def simulate_board(board, start, start_dir = "^"):
    pos = start
    dir = start_dir

    while is_pos_within_bounds(board, pos):
        board = set_val_at_pos(board, pos, "X")
        
        board, pos, dir = simulate_step(board, pos, dir)
        print(pos)

    return board


board = [[x for x in line.strip()] for line in input_lines]
start_pos = None

for i, row in enumerate(board):
    if start_pos is None and "^" in row:
        start_pos = (i, row.index("^"))

board = set_val_at_pos(board, start_pos, ".")

board = simulate_board(board, start_pos)

count = 0
for row in board:
    print("".join(row))
    count += row.count("X")

print(count)
