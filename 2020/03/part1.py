import os

import periodic_grid


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    grid_data = [line.strip() for line in f]
    
grid = periodic_grid.PeriodicGrid(grid_data)

slope = 3
tree_count = 0
for y in range(grid.grid_height):
    if grid.is_tree(slope * y, y):
        tree_count += 1
        
print(f"{tree_count} trees encountered")
