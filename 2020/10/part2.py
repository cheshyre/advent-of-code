import os

import jolt


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    values = [int(x.strip()) for x in f]
values.append(0)
    
values = sorted(values)
values.append(values[-1] + 3)

print(f"There are {jolt.paths_reconstruction(values)} ways to combine the adapters.")
