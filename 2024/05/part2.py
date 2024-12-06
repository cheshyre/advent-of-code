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


def reorder_sequence(rules, ups):
    if len(ups) == 0:
        return []
    
    upss = set(ups)
    
    relevant_rules = [(b, a) for b, a in rules if b in upss and a in upss]
    afters = set([a for _, a in relevant_rules])

    for i, x in enumerate(ups):
        if x not in afters:
            return [x] + reorder_sequence(relevant_rules, ups[:i] + ups[i+1:])
        


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
    if not valid:
        ro_ups = reorder_sequence(rules, ups)
        total += ro_ups[len(ro_ups) // 2]
    
print(total)
