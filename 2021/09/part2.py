import os
from typing import List, Tuple


cur_dir = os.path.dirname(os.path.abspath(__file__))


neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check_bounds(grid, x, y) -> bool:
    if x < 0 or y < 0:
        return False
    if x >= len(grid):
        return False
    if y >= len(grid[x]):
        return False
    return True


def mark_basin(sink, grid, marking) -> Tuple[List[List[bool]], int]:
    marking[sink[0]][sink[1]] = True
    queue = [sink]
    size = 1
    while len(queue) != 0:
        cur_val = queue[0]
        queue = queue[1:]

        x, y = cur_val

        for dx, dy in neighbors:
            if check_bounds(grid, x + dx, y + dy):
                if not marking[x + dx][y + dy]:
                    size += 1
                    marking[x + dx][y + dy] = True
                    queue.append((x + dx, y + dy))

    return marking, size


with open(f"{cur_dir}/input") as f:
    grid = [[int(x) for x in line.strip()] for line in f]

risk_points = []
risk_vals = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        neighbor_heights = [
            grid[i + x][j + y]
            for x, y in neighbors
            if i + x >= 0 and i + x < len(grid) and j + y >= 0 and j + y < len(grid[i])
        ]
        if grid[i][j] < min(neighbor_heights):
            risk_points.append((i, j))
            risk_vals.append(grid[i][j])

marking = [[True if point == 9 else False for point in row] for row in grid]

basin_sizes = [0] * len(risk_points)
for i, pt in enumerate(risk_points):
    marking, size = mark_basin(pt, grid, marking)
    basin_sizes[i] = size

sorted_sizes = list(reversed(sorted(basin_sizes)))

print(sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2])
