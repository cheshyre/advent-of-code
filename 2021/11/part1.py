import os
from typing import List, Tuple


cur_dir = os.path.dirname(os.path.abspath(__file__))

NEIGHBORS = [
    (1, -1),
    (1, 0),
    (1, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (0, -1),
]


def visualize_grid(grid):
    for line in grid:
        print("".join([str(x) if x <= 9 else "x" for x in line]))


def get_neighbor_pts(grid, pt) -> List[Tuple[int, int]]:
    x, y = pt
    return [
        (x + dx, y + dy)
        for dx, dy in NEIGHBORS
        if x + dx < len(grid)
        and x + dx >= 0
        and y + dy < len(grid[x + dx])
        and y + dy >= 0
    ]


def perform_flash(pt, grid) -> Tuple[List[List[int]], List[Tuple[int, int]]]:
    for i, j in get_neighbor_pts(grid, pt):
        grid[i][j] += 1
    new_flashes = [(i, j) for i, j in get_neighbor_pts(grid, pt) if grid[i][j] == 10]

    return grid, new_flashes


def perform_step(grid) -> Tuple[List[List[int]], int]:

    print("start:")
    visualize_grid(grid)

    grid = [[x + 1 for x in row] for row in grid]
    dim_x = len(grid)
    dim_y = len(grid[0])

    print("incremented:")
    visualize_grid(grid)

    flash_pts = [(i, j) for j in range(dim_y) for i in range(dim_x) if grid[i][j] == 10]

    num_flashes = 0

    while len(flash_pts) > 0:
        grid, new_flashes = perform_flash(flash_pts[0], grid)

        flash_pts = flash_pts[1:] + new_flashes
        num_flashes += 1

    print("full flash:")
    visualize_grid(grid)

    grid = [[0 if x > 9 else x for x in row] for row in grid]

    print("end:")
    visualize_grid(grid)

    return grid, num_flashes


with open(f"{cur_dir}/input") as f:
    grid = [[int(x) for x in line.strip()] for line in f]

tot = 0
for i in range(100):
    grid, num_flashes = perform_step(grid)
    print(num_flashes)
    tot += num_flashes

print(tot)
