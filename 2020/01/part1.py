import os

import target_dict


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    components = [int(line) for line in f]
    
targets = target_dict.create_target_dict_pairs(components, 2020)
for f in components:
    if f in targets:
        print(f"Found pair: {f}, {targets[f]}")
        print(f"Product: {f * targets[f]}")
        break
        