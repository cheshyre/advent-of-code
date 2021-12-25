import os
from typing import List, Tuple

cur_dir = os.path.dirname(os.path.abspath(__file__))


def is_empty(grid, i, j) -> bool:
    return grid[i][j] == "."


def get_right_coordinate(grid, i, j) -> Tuple[int, int]:
    return i, (j + 1) % len(grid[i])


def get_below_coordinate(grid, i, j) -> Tuple[int, int]:
    return (i + 1) % len(grid), j


def update_grid(grid) -> Tuple[List[List[str]], int]:
    new_grid = [["." for _ in row] for row in grid]

    num_moves = 0
    for i, row in enumerate(grid):
        for j, cucumber in enumerate(row):
            if cucumber == ">":
                next_i, next_j = get_right_coordinate(grid, i, j)
                if is_empty(grid, next_i, next_j):
                    num_moves += 1
                    new_grid[next_i][next_j] = ">"
                else:
                    new_grid[i][j] = ">"
            elif cucumber == "v":
                new_grid[i][j] = "v"
    new_new_grid = [["." for _ in row] for row in new_grid]
    for i, row in enumerate(new_grid):
        for j, cucumber in enumerate(row):
            if cucumber == ">":
                new_new_grid[i][j] = ">"
            elif cucumber == "v":
                next_i, next_j = get_below_coordinate(new_grid, i, j)
                if is_empty(new_grid, next_i, next_j):
                    num_moves += 1
                    new_new_grid[next_i][next_j] = "v"
                else:
                    new_new_grid[i][j] = "v"
    return new_new_grid, num_moves


def print_grid(grid):
    for row in grid:
        print("".join(row))


with open(f"{cur_dir}/input") as f:
    grid = [[x for x in line.strip()] for line in f]

# print_grid(grid)
num_moves = 0
iter_count = 0
while iter_count == 0 or num_moves != 0:
    grid, num_moves = update_grid(grid)
    iter_count += 1
    print(iter_count)
    # print_grid(grid)

print(iter_count)
