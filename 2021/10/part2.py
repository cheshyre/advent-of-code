import os
from typing import List, Tuple


cur_dir = os.path.dirname(os.path.abspath(__file__))

CLOSE = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

OPEN = {CLOSE[x]: x for x in CLOSE}

SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
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


def get_closing_characters_of_incomplete_line(line) -> List[str]:

    stack = []

    for x in line:
        if x in OPEN:
            stack.append(x)
        elif x in CLOSE:
            if stack.pop() != CLOSE[x]:
                raise Exception("Closing character does not match expected.")
        else:
            raise Exception(f'Invalid character "{x}"')

    return list(reversed([OPEN[x] for x in stack]))


def get_closing_characters_score(characters) -> int:
    score = 0
    for x in characters:
        score *= 5
        score += SCORES[x]

    return score


with open(f"{cur_dir}/input") as f:
    lines = [x.strip() for x in f]

lines = [line for line in lines if determine_line_validity_and_score(line)[0]]

line_scores = [
    get_closing_characters_score(get_closing_characters_of_incomplete_line(line))
    for line in lines
]

# No "+ 1" b/c 0-baesd array indexing
midpt = len(line_scores) // 2

print(sorted(line_scores)[midpt])
