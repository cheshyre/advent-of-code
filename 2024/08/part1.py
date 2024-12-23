# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib
from math import sqrt, floor
from functools import lru_cache

def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

input_lines = get_input_lines()


def compute_r2(pt):
    return pt[0]**2 + pt[1]**2


@lru_cache
def get_points_in_circle(r2):

    pts = []
    
    r = floor(sqrt(r2+0.0001))

    for x in range(-1 * r, r + 1, 1):
        y2 = r2 - x**2

        y = floor(sqrt(y2 + 0.00001))
        if x**2 + y**2 == r2:
            pts.append((x, y))
            if y > 0:
                pts.append((x, -1 * y))
    
    return pts


def compute_r2(pt1, pt2):
    x = abs(pt1[0] - pt2[0])
    y = abs(pt1[1] - pt2[1])

    return x**2 + y**2


def get_diff(pt1, pt2):
    x = pt1[0] - pt2[0]
    y = pt1[1] - pt2[1]

    return x, y


def multiply_diff(diff, factor):
    return int(diff[0] * factor), int(diff[1] * factor)


def add_pts(pt, diff):
    return pt[0] + diff[0], pt[1] + diff[1]


def read_pt(grid, pt):
    dimx = len(grid)
    dimy = 0
    if dimx > 0:
        dimy = len(grid[0])
    
    if pt[0] < 0 or pt[1] < 0 or pt[0] >= dimx or pt[1] >= dimy:
        return "."
    
    # print((dimx, dimy))
    # print(pt)
    
    return grid[pt[0]][pt[1]]


grid = [[x for x in line.strip()] for line in input_lines]
grid_new = [[x for x in line.strip()] for line in input_lines]
dimx = len(grid)
dimy = 0
if dimx > 0:
    dimy = len(grid[0])


def check_antinode(grid, pt):
    dimx = len(grid)
    dimy = 0
    if dimx > 0:
        dimy = len(grid[0])

    for i in range(dimx):
        for j in range(dimy):
            a_pt = (i, j)
            if a_pt == pt:
                continue

            if read_pt(grid, a_pt) != ".":
                # We have antenna at i, j
                antenna_char = read_pt(grid, a_pt)
                
                r2 = compute_r2(pt, a_pt)

                diff = get_diff(a_pt, pt)

                print(f"Found antenna {antenna_char} at {a_pt}, {diff} relative to {pt}")

                cands = [
                    multiply_diff(diff, 2),
                    multiply_diff(diff, -2),
                ]
                    
                # if r2 % 4 == 0:
                if diff[0] % 2 == 0 and diff[1] % 2 == 0:
                    cands.append(multiply_diff(diff, 0.5))
                    cands.append(multiply_diff(diff, -0.5))

                for new_diff in cands:

                    new_pt = add_pts(pt, new_diff)

                    print(f"Searching at {new_pt}, {new_diff} relative to {pt}")

                    if read_pt(grid, new_pt) == antenna_char:
                        print("Pattern for interference found")
                        return True
                        
    return False

# check_antinode(grid, (0, 7))
an_count = 0
for i in range(dimx):
    for j in range(dimy):
        # print(f"Checking {(i, j)}")
        if check_antinode(grid, (i, j)):
            grid_new[i][j] = "#"
            print((i, j))
            an_count += 1

print(an_count)
# for row in grid_new:
#     print("".join(row))



