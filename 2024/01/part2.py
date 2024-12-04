# Copyright (c) 2024 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pathlib


def get_input_lines():
    input_file = pathlib.Path(__file__).parent / "input"

    with open(input_file) as fin:
        return [line.strip() for line in fin]
    

def sort_list(l):
    return list(sorted(l))


def make_locations(l):
    locations = {}

    for i, val in enumerate(l):
        if val not in locations:
            locations[val] = []
        locations[val].append(i)
    
    return locations
    

input_lines = get_input_lines()

left_list = [int(x.split()[0]) for x in input_lines]
right_list = [int(x.split()[1]) for x in input_lines]

left_list_sorted = sort_list(left_list)
right_list_sorted = sort_list(right_list)

left_list_locs = make_locations(left_list)
right_list_locs = make_locations(right_list)

dist = 0
for l in left_list:
    if l in right_list_locs:
        dist += l * len(right_list_locs[l])

print(dist)
