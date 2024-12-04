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
print(left_list_locs)
right_list_locs = make_locations(right_list)

dist = 0
for l, r in zip(left_list_sorted, right_list_sorted):
    print("L = ", l)
    print("R = ", r)
    il = left_list_locs[l][0]
    left_list_locs[l] = left_list_locs[l][1:]
    ir = right_list_locs[r][0]
    right_list_locs[r] = right_list_locs[r][1:]
    # print("iL = ", il)
    # print("iR = ", ir)
    print("d = ", abs(l - r))

    dist += abs(l - r)

print(dist)
