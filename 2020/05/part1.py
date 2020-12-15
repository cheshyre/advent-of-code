import os

import boarding_pass


cur_dir = os.path.dirname(os.path.abspath(__file__))

max_seat_id = 0
with open(f"{cur_dir}/input") as f:
    for line in f:
        boarding = line.strip()
        max_seat_id = max(max_seat_id, boarding_pass.get_boarding_pass_seat_id(boarding))
        
print(f"Max seat id is {max_seat_id}")
