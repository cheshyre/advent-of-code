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


def set_val_at_pos(board, pos, dir):
    board[pos[0]][pos[1]][dir] = True
    return board


def print_board(board):
    for row in board:
        for entry in row:
            multiple_trues = len(
                [x for x in DIRS if entry[x]]
            ) > 1
            one_true = len(
                [x for x in DIRS if entry[x]]
            ) == 1
            if entry["#"]:
                print("#", end="")
            elif entry["X"]:
                print("X", end="")
            elif entry["O"]:
                print("O", end="")
            elif multiple_trues:
                print("+", end="")
            elif one_true:
                print("".join([x for x in DIRS if entry[x]]), end="")
            else:
                print(".", end="")
        print("")


def simulate_ray(board, pos, dir):
    # print("-" * 20)
    # print_board(board)
    # print("-" * 20)
    while is_pos_within_bounds(board, pos) and not (get_val_at_pos(board, pos)["#"] or get_val_at_pos(board, pos)["O"]):
        board = set_val_at_pos(board, pos, dir)
        # print("-" * 20)
        # print_board(board)
        # print("-" * 20)
        old_pos = pos
        pos = add_pos(pos, DIRS_COORDS[dir])
        if is_pos_within_bounds(board, pos):
            if get_val_at_pos(board, pos)["#"] or get_val_at_pos(board, pos)["O"]:
                new_dir = DIRS[
                    (DIRS.index(dir) + 1) % len(DIRS)
                ]
                return board, old_pos, new_dir
        else:
            return board, pos, dir
    # return board, pos, dir


def copy_board(board):
    return [[{k: entry[k] for k in entry} for entry in row] for row in board]


def simulate_board_blocking_next_has_loop(board, start, start_dir):
    # board = [[{k: entry[k] for k in entry} for entry in row] for row in board]
    pos = start
    dir = start_dir
    # new_pos = add_pos(pos, DIRS_COORDS[dir])
    # if not is_pos_within_bounds(board, new_pos):
    #     return False, (0, 0)
    # board = set_val_at_pos(board, new_pos, "O")

    while is_pos_within_bounds(board, pos):
        if get_val_at_pos(board, pos)[dir]:
            board = set_val_at_pos(board, pos, "X")
            print("Loop found")
            # print_board(board)
            # This is a loop
            return True
        board = set_val_at_pos(board, pos, dir)
        
        board, pos, dir = simulate_ray(board, pos, dir)

    return False


def simulate_board(board, start, start_dir = "^"):
    pos = start
    dir = start_dir

    # loop_count = 0
    loop_blockers = set()
    while is_pos_within_bounds(board, pos):
        if get_val_at_pos(board, pos)[dir]:
            # This is a loop
            print("Loop found")
            pass
        loop_found, loop_blocker = simulate_board_blocking_next_has_loop(board, pos, dir)
        if loop_found:
            loop_blockers.add(loop_blocker)
            loop_count += 1
        board = set_val_at_pos(board, pos, dir)
        
        board, pos, dir = simulate_ray(board, pos, dir)

    return board, len(loop_blockers)


board = [[{y: False for y in DIRS + ["#", "X", "O"]} for _ in line.strip()] for line in input_lines]
for i, line in enumerate(input_lines):
    for j, c in enumerate(line.strip()):
        if c in DIRS + ["#"]:
            board[i][j][c] = True
start_pos = None

for i, row in enumerate(board):
    for j, entry in enumerate(row):
        if start_pos is None and entry["^"]:
            start_pos = (i, j)
            entry["^"] = False

# board = set_val_at_pos(board, start_pos, ".")

loop_count = 0
for i, row in enumerate(board):
    for j, _ in enumerate(row):
        if (i, j) == start_pos:
            continue
        if get_val_at_pos(board, (i, j))["#"]:
            continue
        temp_board = copy_board(board)
        temp_board = set_val_at_pos(temp_board, (i, j), "O")
        loop_found = simulate_board_blocking_next_has_loop(temp_board, start_pos, "^")
        if loop_found:
            loop_count += 1
print(loop_count)

# count = 0
# for row in board:
#     for entry in row:
#         multiple_trues = len(
#             [x for x in DIRS if entry[x]]
#         ) > 1
#         one_true = len(
#             [x for x in DIRS if entry[x]]
#         ) == 1
#         if entry["#"]:
#             print("#", end="")
#         elif multiple_trues:
#             print("+", end="")
#             count += 1
#         elif one_true:
#             print("".join([x for x in DIRS if entry[x]]), end="")
#             count += 1
#         else:
#             print(".", end="")
#     print("")
#     # print("".join(row))
#     # for dir in DIRS:
#     #     count += row.count(dir)

# print(count)
