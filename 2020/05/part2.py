import os

import boarding_pass


cur_dir = os.path.dirname(os.path.abspath(__file__))

seat_ids = []
with open(f"{cur_dir}/input") as f:
    for line in f:
        boarding = line.strip()
        seat_ids.append(boarding_pass.get_boarding_pass_seat_id(boarding))

seat_ids.sort()

for i, x in enumerate(seat_ids[:-1]):
    if seat_ids[i + 1] != x + 1:
        print(f"Your seat id is {x + 1}")
        break
    