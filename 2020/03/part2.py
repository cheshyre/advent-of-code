import os

import periodic_grid


def apply_slope(input, slope):
    return (input[0] + slope[0], input[1] + slope[1])


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    grid_data = [line.strip() for line in f]
    
grid = periodic_grid.PeriodicGrid(grid_data)

slopes = [
    (1, 1), 
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
tree_counts = []

for slope in slopes:
    tree_count = 0
    
    cur_axes = apply_slope((0, 0), slope)
    while cur_axes[1] < grid.grid_height:
        if grid.is_tree(cur_axes[0], cur_axes[1]):
            tree_count += 1
            
        cur_axes = apply_slope(cur_axes, slope)
        
    print(f"{tree_count} trees encountered")
    tree_counts.append(tree_count)
    
prod_val = 1
for x in tree_counts:
    prod_val *= x
    
print(f"Product of trees encounter is {prod_val}")
