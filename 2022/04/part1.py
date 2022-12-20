# Copyright (c) 2022 Matthias Heinz
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import tqdm
import os
import string

class Pair:

    def __init__(self, a, b):
        self._min = min(a, b)
        self._max = max(a, b)
    
    def min(self):
        return self._min
    
    def max(self):
        return self._max

    def contains(self, other):
        return (self.min() <= other.min()) and (self.max() >= other.max())

    def is_contained_in(self, other):
        my_set = set(list(range(self.min(), self.max() + 1)))
        other_set = set(list(range(other.min(), other.max() + 1)))

        return len(my_set.difference(other_set)) == 0

    def __repr__(self) -> str:
        return "{}".format((self.min(), self.max()))


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    input = [x.strip() for x in f]

overlap_count = 0

for line in tqdm.tqdm(input):
    pair1 = [int(x) for x in line.split(",")[0].split("-")]
    # print(pair1)
    pair2 = [int(x) for x in line.split(",")[1].split("-")]
    # print(pair2)
    pair1 = Pair(pair1[0], pair1[1])
    pair2 = Pair(pair2[0], pair2[1])

    # if pair1.is_contained_in(pair2) or pair2.is_contained_in(pair1):
    if pair1.contains(pair2) or pair2.contains(pair1):
        overlap_count += 1
    else:
        print(pair1)
        print(pair2)

print(overlap_count)