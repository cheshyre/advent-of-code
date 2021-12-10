import os
from typing import Tuple


cur_dir = os.path.dirname(os.path.abspath(__file__))

OPEN = set(["(", "[", "{", "<"])

CLOSE = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def determine_line_validity_and_score(line) -> Tuple[bool, int]:

    stack = []

    for x in line:
        if x in OPEN:
            stack.append(x)
        elif x in CLOSE:
            if stack.pop() != CLOSE[x]:
                return False, SCORES[x]
        else:
            raise Exception(f'Invalid character "{x}"')

    return True, 0


with open(f"{cur_dir}/input") as f:
    lines = [x.strip() for x in f]

total_score = 0
for line in lines:
    valid, score = determine_line_validity_and_score(line)
    total_score += score

print(total_score)
