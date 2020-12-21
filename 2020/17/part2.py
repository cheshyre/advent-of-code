import os

import hypercube


cur_dir = os.path.dirname(os.path.abspath(__file__))

z = 0
w = 0
active_dict = {}
with open(f"{cur_dir}/input") as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "#":
                active_dict[(x, y, z, w)] = hypercube.HyperCube(x, y, z, w)

active_dict = hypercube.determine_next_active_dict(active_dict)
active_dict = hypercube.determine_next_active_dict(active_dict)
active_dict = hypercube.determine_next_active_dict(active_dict)
active_dict = hypercube.determine_next_active_dict(active_dict)
active_dict = hypercube.determine_next_active_dict(active_dict)
active_dict = hypercube.determine_next_active_dict(active_dict)

hypercube.draw_state(active_dict)
print(f"There are {len(active_dict)} active hypercubes after the six-cycle boot.")
