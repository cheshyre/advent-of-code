import os

import hex_grid


cur_dir = os.path.dirname(os.path.abspath(__file__))

tiles_count = {}
with open(f"{cur_dir}/input") as f:
    for line in f:
        instrs = hex_grid.parse_instructions(line)
        point = (0, 0)
        for i in instrs:
            point = hex_grid.apply_instruction_to_point(point, i)
        if point in tiles_count:
            del tiles_count[point]
        else:
            tiles_count[point] = 1

for _ in range(100):
    tiles_count = hex_grid.do_step(tiles_count)
    
print(f"After 100 days there are {len(tiles_count)} black tiles.")
