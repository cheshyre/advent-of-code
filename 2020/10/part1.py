import os

import jolt


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    values = [int(x.strip()) for x in f]
values.append(0)
    
values = sorted(values)
diffs = jolt.make_differences(values)
diffs_1s = diffs.count(1)
diffs_3s = diffs.count(3) + 1

print(f"Found {diffs_1s} 1-jolt differences")
print(f"Found {diffs_3s} 3-jolt differences")
print(f"The product is {diffs_1s * diffs_3s}")
