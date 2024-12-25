# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib
from math import sqrt, floor
from functools import lru_cache

def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

input_lines = get_input_lines()

input_line = input_lines[0]


def parse_blocks(line):
    storage = True

    blocks = {}
    id = 0
    loc = 0
    for v in line.strip():
        v = int(v)
        if storage:
            blocks[id] = (loc, loc + v)
            id += 1
        storage = not storage
        loc += v

    return blocks

blocks = parse_blocks(input_line)


def populate_initial_memory(blocks):
    total_mem = sum([blocks[x][1] - blocks[x][0] for x in blocks])
    # total_mem = max([blocks[id][1] for id in blocks])

    mem = [-1] * total_mem

    blocks_beyond_mem = {}
    for id in blocks:
        for loc in range(blocks[id][0], blocks[id][1]):
            if loc < total_mem:
                mem[loc] = id
            else:
                blocks_beyond_mem[loc] = id

    print(loc + 1)
    mem += [-1] * (loc + 1 - total_mem)
    return mem, blocks_beyond_mem


def move_memory(mem, blocks_beyond_mem):

    loc = 0

    for oob_loc in reversed(sorted([x for x in blocks_beyond_mem])):
        loc = mem.index(-1, loc)

        mem[loc] = blocks_beyond_mem[oob_loc]
    
    return mem

mem, bbm = populate_initial_memory(blocks)
mem = move_memory(mem, bbm)


def compute_hash(mem):
    myhash = 0
    for i, v in enumerate(mem):
        if v != -1:
            myhash += i * v

    return myhash


print(compute_hash(mem))
