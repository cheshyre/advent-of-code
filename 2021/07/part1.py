import os
from typing import Sequence


cur_dir = os.path.dirname(os.path.abspath(__file__))


def get_fuel_cost(positions: Sequence[int], align_position: int) -> int:
    return sum([abs(x - align_position) for x in positions])


with open(f"{cur_dir}/input") as f:
    positions = [int(x) for x in f.readline().strip().split(",")]


min_pos = min(positions)
max_pos = max(positions)

align_candidates = list(range(min_pos, max_pos + 1))
align_costs = [get_fuel_cost(positions, x) for x in align_candidates]

print(min(align_costs))
