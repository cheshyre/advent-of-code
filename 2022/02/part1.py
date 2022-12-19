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
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
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

def eval_move(x, y):
    y = MY_MOVE_MAP[y]
    x = OPP_MOVE_MAP[x]
    win = ((MOVE_IDS[y] - MOVE_IDS[x] + 9) % 3 == 1)
    draw = ((MOVE_IDS[y] - MOVE_IDS[x] + 9) % 3 == 0)
    lose = ((MOVE_IDS[y] - MOVE_IDS[x] + 9) % 3 - 3 == -1)
    score = 0
    if win:
        score += 6
    if draw:
        score += 3
    score += MOVE_SCORES[y]
    return score

print(sum([eval_move(x, y) for x, y in zip(opp_moves, my_moves)]))
