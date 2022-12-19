# Copyright (c) 2022 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import tqdm
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    input = [x.strip() for x in f]

elf_calories_items = []
cur_elf = []
for val in tqdm.tqdm(input):
    if val == "":
        elf_calories_items.append(cur_elf)
        cur_elf = []
    else:
        cur_elf.append(int(val))
if len(cur_elf) > 0:
    elf_calories_items.append(cur_elf)
    cur_elf = []

elf_calories = sorted([sum(x) for x in elf_calories_items])
print(elf_calories[-3:])
print(sum(elf_calories[-3:]))
