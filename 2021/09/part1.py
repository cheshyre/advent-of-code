import os


cur_dir = os.path.dirname(os.path.abspath(__file__))


with open(f"{cur_dir}/input") as f:
    grid = [[int(x) for x in line.strip()] for line in f]

neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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

print(sum(risk_vals) + len(risk_vals))