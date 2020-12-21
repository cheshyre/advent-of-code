import os

import cube


cur_dir = os.path.dirname(os.path.abspath(__file__))

z = 0
active_dict = {}
with open(f"{cur_dir}/input") as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "#":
                active_dict[(x, y, z)] = cube.Cube(x, y, z)

active_dict = cube.determine_next_active_dict(active_dict)
active_dict = cube.determine_next_active_dict(active_dict)
active_dict = cube.determine_next_active_dict(active_dict)
active_dict = cube.determine_next_active_dict(active_dict)
active_dict = cube.determine_next_active_dict(active_dict)
active_dict = cube.determine_next_active_dict(active_dict)

cube.draw_state(active_dict)
print(f"There are {len(active_dict)} active cubes after the six-cycle boot.")
