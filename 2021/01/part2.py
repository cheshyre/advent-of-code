import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    depths = [int(x) for x in f]
    
windows = [0] * (len(depths) - 2)
for i in range(len(windows)):
    windows[i] = sum(depths[i:i+3])
    
num_depth_increases = 0
for i in range(1, len(windows)):
    if windows[i] > windows[i - 1]:
        num_depth_increases += 1

print(num_depth_increases)
