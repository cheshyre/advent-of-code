# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib


def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

input_lines = get_input_lines()

input_rows = [[int(x) for x in line.split()] for line in input_lines]


def determine_if_row_is_safe(row):
    increasing = False
    decreasing = False

    prev = row[0]
    for val in row[1:]:
        if abs(val - prev) > 3:
            return False
        if val > prev:
            increasing = True
        elif val < prev:
            decreasing = True
        else:
            return False

        if increasing and decreasing:
            return False
        
        prev = val

    return True

count = 0
for row in input_rows:
    if determine_if_row_is_safe(row):
        count += 1

print(count)

