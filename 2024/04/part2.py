# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib
import re


def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

grid = [[x for x in line] for line in get_input_lines()]


def check_xmas_at_coord_with_offset(i, j, grid, offset):
    ud, rl = offset
    dimx = len(grid[0])
    dimy = len(grid)

    for x, c in enumerate("MAS"):
        xx = x - 1
        ii = i + xx * ud
        jj = j + xx * rl
        if ii < 0 or ii >= dimy:
            return 0
        if jj < 0 or jj >= dimx:
            return 0
        if grid[ii][jj] != c:
            return 0
    
    return 1


def count_xmas_at_coord(i, j, grid):
    total = 0

    for offset in [
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1),
    ]:
        total += check_xmas_at_coord_with_offset(i, j, grid, offset)
    
    if total == 2:
        return 1
    return 0

full_total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        full_total += count_xmas_at_coord(i, j, grid)
    
print(full_total)
