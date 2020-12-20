import os

import counting


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    input_vals = [int(x) for x in f.readline().strip().split(",")]
    
last_called_dict = {}
for i, x in enumerate(input_vals[:-1]):
    last_called_dict[x] = i
last_called_num = input_vals[-1]
iteration = len(input_vals)

while iteration != 2020:
    last_called_dict, last_called_num, iteration = counting.do_step(last_called_dict, last_called_num, iteration)
print(iteration)
print(last_called_num)
# print(last_called_dict)
