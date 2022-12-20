# Copyright (c) 2022 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import tqdm
import os
import string

cur_dir = os.path.dirname(os.path.abspath(__file__))

ORDERED_ITEMS = [x for x in string.ascii_lowercase] + [x for x in string.ascii_uppercase]
PRIORITIES = {x : i + 1 for i, x in enumerate(ORDERED_ITEMS)}

print(PRIORITIES)

with open(f"{cur_dir}/input") as f:
    input = [x.strip() for x in f]

priority_sum = 0
for line in tqdm.tqdm(input):
    bagsize = len(line) // 2
    bag1 = [val for val in line[:bagsize]]
    bag2 = [val for val in line[bagsize:]]
    bag1_elems = set(bag1)
    bag2_elems = set(bag2)
    common_elem = bag1_elems.intersection(bag2_elems).pop()
    priority_sum += PRIORITIES[common_elem]

print(priority_sum)
