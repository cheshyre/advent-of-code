import os

import sum_check


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    values = [int(x.strip()) for x in f]
    
for i in range(25, len(values)):
    val = values[i]
    sum_vals = sum_check.get_all_sum_vals(values[i-25:i])
    if val not in sum_vals:
        break

print(f"The first value that does not fulfill condition is {val}")