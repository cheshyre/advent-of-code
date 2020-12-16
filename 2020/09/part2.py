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
    
for i in range(len(values)):
    end_pt = sum_check.identify_cont_set(val, values[i:])
    if end_pt != -1:
        min_val = min(values[i:i + end_pt + 1])
        max_val = max(values[i:i + end_pt + 1])
        break
        
print(f"Encryption weakness is {min_val + max_val}")
