# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib
import re


def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

input_lines = get_input_lines()


def parse_rules(input_lines):
    rules = []
    for line in input_lines:
        if "|" in line:
            rules.append(tuple([int(x) for x in line.split("|")]))

    return rules


def parse_updates(input_lines):
    updates = []
    for line in input_lines:
        if "," in line:
            update_seq = [int(x) for x in line.split(",")]
            update_seq_locs = {x: i for i, x in enumerate(update_seq)}

            updates.append((update_seq, update_seq_locs))

    return updates

rules = parse_rules(input_lines)
updates = parse_updates(input_lines)

total = 0
for ups, upsl in updates:
    valid = True
    for b, a in rules:
        if not valid:
            break
        if b in upsl and a in upsl:
            if upsl[b] > upsl[a]:
                valid = False
    if valid:
        print(ups)
        total += ups[len(ups) // 2]
    
print(total)
