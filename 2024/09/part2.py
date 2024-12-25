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

    blocks_new = []
    id = 0
    loc = 0
    l = line.strip()
    block_sizes = [int(l[i]) for i in range(0, len(l), 2)]
    block_gaps = [int(l[i]) for i in range(1, len(l), 2)]
    while len(block_gaps) < len(block_sizes):
        block_gaps.append(0)

    for s, g in zip(block_sizes, block_gaps):
        blocks_new.append(
            {
                "id": id,
                "start": loc,
                "size": s,
                "gap": g,
            }
        )
        id += 1
        loc += s + g

    return blocks_new

blocks = parse_blocks(input_line)
print(blocks)

def move_memory(blocks):
    ids_reverse = list(reversed(sorted(x["id"] for x in blocks)))
    id_locs = {blocks[i]["id"]: i for i in range(len(blocks))}

    for id in ids_reverse:
        b2m = blocks[id_locs[id]]
        b2m_loc = id_locs[id]
        tg = b2m["size"]
        for loc in range(len(blocks)):
            if loc >= b2m_loc:
                break
            b = blocks[loc]
            if b["gap"] >= tg:
                print(f"Moving {id} from {b2m_loc} (size: {tg}) to {loc + 1} (gap: {b["gap"]})")
                new_block = {
                    "id": id,
                    "start": b["start"] + b["size"],
                    "size": b2m["size"],
                    "gap": b["gap"] - b2m["size"],
                }
                blocks[loc]["gap"] = 0

                blocks = blocks[:loc + 1] + [new_block] + blocks[loc + 1:b2m_loc] + blocks[b2m_loc + 1:]
                # print(blocks)
                id_locs = {blocks[i]["id"]: i for i in range(len(blocks))}

                break

    return blocks

blocks = move_memory(blocks)
# print(blocks)

# def populate_initial_memory(blocks):
#     total_mem = max([blocks[id][1] for id in blocks])

#     mem = [-1] * total_mem

#     blocks_beyond_mem = {}
#     for id in blocks:
#         for loc in range(blocks[id][0], blocks[id][1]):
#             if loc < total_mem:
#                 mem[loc] = id
#             else:
#                 blocks_beyond_mem[loc] = id

#     return mem, blocks_beyond_mem


# def compute_gaps(mem):
#     gap = False
#     gap_start = 0

#     gaps = {}
#     for i, v in enumerate(mem):
#         if not gap and v == -1:
#             gap = True
#             gap_start = i
#         elif gap and v != -1:
#             gap = False
#             gap_len = i - gap_start
#             if gap_len not in gaps:
#                 gaps[gap_len] = []
#             gaps[gap_len].append(gap_start)
    
#     return gaps


# def move_memory(mem, blocks):
#     for id in reversed(sorted([x for x in blocks])):
#         # if id < 9950:
#         #     continue
#         block_len = blocks[id][1] - blocks[id][0]
#         block_loc = blocks[id][0]

#         gaps = compute_gaps(mem)

#         moved = False
#         for gap_size in range(block_len, len(mem)):
#             if moved:
#                 continue
#             if gap_size in gaps:
#                 gap_loc = gaps[gap_size][0]

#                 if gap_loc < block_loc:
#                     mem[gap_loc: gap_loc + block_len] = [id] * block_len
#                     mem[block_loc: block_loc + block_len] = [-1] * block_len
#                     moved = True
                
#         print(",".join([f"{x:>4}".replace("-1", " .") for x in mem[:100]]))

#     return mem

# mem, bbm = populate_initial_memory(blocks)
# mem = move_memory(mem, blocks)


def compute_hash(blocks):
    myhash = 0
    for b in blocks:
        id = b["id"]

        for ind in range(b["start"], b["start"] + b["size"]):
            myhash += id * ind

    return myhash


print(compute_hash(blocks))
