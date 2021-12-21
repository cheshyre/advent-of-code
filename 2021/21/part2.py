import os

import numpy as np


MAX_SCORE = 21

TRACK_SIZE = 10

THREE_ROLL_SUM = [
    x + y + z for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)
]

THREE_ROLL_DIST = {x: THREE_ROLL_SUM.count(x) for x in THREE_ROLL_SUM}


def num_connections(pos, next_pos):
    pos_diff = normalize_position(next_pos - pos)

    if pos_diff in THREE_ROLL_DIST:
        return THREE_ROLL_DIST[pos_diff]

    return 0


def normalize_position(pos_m1):

    if pos_m1 >= TRACK_SIZE:
        return pos_m1 % TRACK_SIZE

    if pos_m1 < 0:
        return pos_m1 + 10

    return pos_m1


def populate_row(num_paths, row_index):

    for pos_m1 in range(len(num_paths[row_index])):
        for score in range(len(num_paths[row_index][pos_m1])):
            prev_score = score - (pos_m1 + 1)

            if prev_score >= MAX_SCORE:
                continue
            if prev_score < 0:
                continue

            val = 0
            for prev_pos_m1 in range(len(num_paths[row_index - 1])):
                val += (
                    num_connections(prev_pos_m1, pos_m1)
                    * num_paths[row_index - 1][prev_pos_m1][prev_score]
                )

            num_paths[row_index][pos_m1][score] = val

    return num_paths


def determine_number_of_wins(
    num_paths_winner, num_paths_loser, row_index, loser_row_offset
):
    sum_paths_winner = sum(
        [
            num_paths_winner[row_index][pos_m1][score]
            for pos_m1 in range(TRACK_SIZE)
            for score in range(MAX_SCORE, MAX_SCORE + TRACK_SIZE)
        ]
    )
    sum_paths_loser = sum(
        [
            num_paths_loser[row_index + loser_row_offset][pos_m1][score]
            for pos_m1 in range(TRACK_SIZE)
            for score in range(0, MAX_SCORE)
        ]
    )

    return sum_paths_winner * sum_paths_loser


def print_num_paths(num_paths, row_index, score_cutoff):

    for score in range(score_cutoff):
        print(f"SCORE = {score}: ", end="")
        print(
            " ".join(
                [
                    str(num_paths[row_index][pos_m1][score])
                    for pos_m1 in range(TRACK_SIZE)
                ]
            )
        )


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    p1_pos = int(f.readline().strip().split()[-1]) - 1
    p2_pos = int(f.readline().strip().split()[-1]) - 1

# index via [round][pos - 1][score]
number_of_paths_p1 = np.zeros(
    (MAX_SCORE + 1, TRACK_SIZE, MAX_SCORE + TRACK_SIZE), dtype=int
)
number_of_paths_p2 = np.zeros(
    (MAX_SCORE + 1, TRACK_SIZE, MAX_SCORE + TRACK_SIZE), dtype=int
)

number_of_paths_p1[0][p1_pos][0] = 1
number_of_paths_p2[0][p2_pos][0] = 1

for row in range(1, MAX_SCORE + 1):
    number_of_paths_p1 = populate_row(number_of_paths_p1, row)
    number_of_paths_p2 = populate_row(number_of_paths_p2, row)

p1_wins = sum(
    [
        determine_number_of_wins(number_of_paths_p1, number_of_paths_p2, row, -1)
        for row in range(MAX_SCORE + 1)
    ]
)
p2_wins = sum(
    [
        determine_number_of_wins(number_of_paths_p2, number_of_paths_p1, row, 0)
        for row in range(MAX_SCORE + 1)
    ]
)

print(p1_wins)
print(p2_wins)

print(max(p1_wins, p2_wins))
