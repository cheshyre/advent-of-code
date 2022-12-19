# Copyright (c) 2022 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import tqdm
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    input = [x.strip() for x in f]

opp_moves = [x.split()[0] for x in input]
my_moves = [x.split()[1] for x in input]


OPP_MOVE_MAP = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

MY_MOVE_MAP = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

MOVE_MAP = {
    "lose": -1,
    "draw": 0,
    "win": 1,
}

MOVE_SCORES = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

MOVE_IDS = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

MOVE_IDS_INV = {MOVE_IDS[x]: x for x in MOVE_IDS}

def eval_move(x, y):
    x = MOVE_IDS[OPP_MOVE_MAP[x]]
    my_offset = MOVE_MAP[MY_MOVE_MAP[y]]
    # sub 1 and add 1 to land in [1, 3] vs [0, 2]
    y_id = (x + my_offset + 6 - 1) % 3 + 1
    y = MOVE_IDS_INV[y_id]
    win = (my_offset == 1)
    draw = (my_offset == 0)
    lose = (my_offset == -1)
    score = 0
    if win:
        score += 6
    if draw:
        score += 3
    score += MOVE_SCORES[y]
    return score

print(sum([eval_move(x, y) for x, y in zip(opp_moves, my_moves)]))
