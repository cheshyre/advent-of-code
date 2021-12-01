import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    depths = [int(x) for x in f]
    
num_depth_increases = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        num_depth_increases += 1

print(num_depth_increases)
