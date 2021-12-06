import os
from typing import Dict, Mapping


def do_step(age_count_map: Mapping[int, int]) -> Dict[int, int]:
    new_map = {}
    for age in age_count_map:
        if age == 0:
            if 6 in new_map:
                new_map[6] += age_count_map[age]
            else:
                new_map[6] = age_count_map[age]
            if 8 in new_map:
                new_map[8] += age_count_map[age]
            else:
                new_map[8] = age_count_map[age]
        else:
            if age - 1 in new_map:
                new_map[age - 1] += age_count_map[age]
            else:
                new_map[age - 1] = age_count_map[age]

    return new_map


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    line = f.readline()

    fish = [int(x) for x in line.strip().split(",")]
    age_count_map = {x: 0 for x in fish}
    for x in age_count_map:
        age_count_map[x] = fish.count(x)

for i in range(256):
    age_count_map = do_step(age_count_map)

print(sum([age_count_map[x] for x in age_count_map]))
