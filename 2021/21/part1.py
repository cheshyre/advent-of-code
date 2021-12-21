import os
from typing import Tuple


def move_player(position, dice_state, score) -> Tuple[int, int, int]:

    move = (
        (dice_state + 1) + ((dice_state + 1) % 100 + 1) + ((dice_state + 2) % 100 + 1)
    )
    final_dice_state = (dice_state + 3) % 100

    position = (position + move) % 10

    score = score + position + 1

    return position, final_dice_state, score


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    p1_pos = int(f.readline().strip().split()[-1]) - 1
    p2_pos = int(f.readline().strip().split()[-1]) - 1

p1_score = 0
p2_score = 0

dice_state = 0

num_dice_rolls = 0
while p1_score < 1000 and p2_score < 1000:
    p1_pos, dice_state, p1_score = move_player(p1_pos, dice_state, p1_score)
    num_dice_rolls += 3
    if p1_score >= 1000:
        break
    p2_pos, dice_state, p2_score = move_player(p2_pos, dice_state, p2_score)
    num_dice_rolls += 3

print(min(p1_score, p2_score) * num_dice_rolls)
