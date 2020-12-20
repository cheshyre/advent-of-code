import os

import mod_calcs


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    arrival_time = int(f.readline().strip())
    buses_full = [(int(x), i) for i, x in enumerate(f.readline().strip().split(',')) if x != "x"]

bus_start = buses_full[0][0]
buses_rest = [x[0] for x in buses_full[1:]]
offsets_rest = [x[1] for x in buses_full[1:]]

print(f"The earliest timestamp is {mod_calcs.get_timestamp(bus_start, buses_rest, offsets_rest)}")
