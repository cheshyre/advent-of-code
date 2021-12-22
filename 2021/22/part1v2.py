import os
from typing import Callable, List, Tuple

import numpy as np
from numpy.core.fromnumeric import var

MIN_REGION = -50
MAX_REGION = 50

REGION_SIZE = MAX_REGION - MIN_REGION + 1
COORD_OFFSET = -1 * MIN_REGION

cur_dir = os.path.dirname(os.path.abspath(__file__))


reactor = np.zeros((REGION_SIZE, REGION_SIZE, REGION_SIZE), dtype=int)


def parse_extents(ext: str) -> Tuple[int, int]:
    return tuple([int(x) for x in ext.split("=")[1].split("..")])


def parse_region(line: str) -> Tuple[int, int, int, int, int, int]:
    extents = line.split(",")
    xmin, xmax = parse_extents(extents[0])
    ymin, ymax = parse_extents(extents[1])
    zmin, zmax = parse_extents(extents[2])

    return xmin, xmax, ymin, ymax, zmin, zmax


def parse_command(line: str) -> Tuple[str, int, int, int, int, int, int]:
    split_line = line.strip().split()
    command = split_line[0]
    extents = split_line[1]

    xmin, xmax, ymin, ymax, zmin, zmax = parse_region(extents)

    return command, xmin, xmax, ymin, ymax, zmin, zmax


def shift_and_normalize_extents(var_min, var_max) -> Tuple[int, int]:
    var_min += COORD_OFFSET
    var_max += COORD_OFFSET

    if var_min < MIN_REGION + COORD_OFFSET:
        var_min = MIN_REGION + COORD_OFFSET
    elif var_min > MAX_REGION + COORD_OFFSET:
        var_min = MAX_REGION + COORD_OFFSET + 1
    if var_max < MIN_REGION + COORD_OFFSET:
        var_max = MIN_REGION + COORD_OFFSET - 1
    elif var_max > MAX_REGION + COORD_OFFSET:
        var_max = MAX_REGION + COORD_OFFSET

    return var_min, var_max


class Block:
    def __init__(
        self, xmin: int, xmax: int, ymin: int, ymax: int, zmin: int, zmax: int
    ) -> None:
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax

    def num_cubes(self) -> int:
        xdiff = self.xmax + 1 - self.xmin
        ydiff = self.ymax + 1 - self.ymin
        zdiff = self.zmax + 1 - self.zmin

        if xdiff <= 0 or ydiff <= 0 or zdiff <= 0:
            return 0

        return xdiff * ydiff * zdiff

    def intersection_data(self) -> Tuple[List[int], List[Callable[[int, int], int]]]:
        return [self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax], [
            max,
            min,
            max,
            min,
            max,
            min,
        ]

    def intersection(self, other: "Block") -> "Block":
        this_extents, int_ops = self.intersection_data()
        other_extents, _ = other.intersection_data()

        int_extents = [
            op(a, b) for a, b, op in zip(this_extents, other_extents, int_ops)
        ]

        xmin, xmax, ymin, ymax, zmin, zmax = tuple(int_extents)

        return Block(xmin, xmax, ymin, ymax, zmin, zmax)

    def subtract(self, other: "Block") -> List["Block"]:
        new_blocks = [
            Block(
                self.xmin, other.xmin - 1, self.ymin, self.ymax, self.zmin, self.zmax
            ),
            Block(
                other.xmax + 1, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax
            ),
            Block(
                other.xmin, other.xmax, self.ymin, other.ymin - 1, self.zmin, self.zmax
            ),
            Block(
                other.xmin, other.xmax, other.ymax + 1, self.ymax, self.zmin, self.zmax
            ),
            Block(
                other.xmin,
                other.xmax,
                other.ymin,
                other.ymax,
                self.zmin,
                other.zmin - 1,
            ),
            Block(
                other.xmin,
                other.xmax,
                other.ymin,
                other.ymax,
                other.zmax + 1,
                self.zmax,
            ),
        ]

        return [x for x in new_blocks if x.num_cubes() != 0]

    def __repr__(self) -> str:
        return str((self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax))


init_block = Block(
    MIN_REGION, MAX_REGION, MIN_REGION, MAX_REGION, MIN_REGION, MAX_REGION
)

on_blocks: List[Block] = []
with open(f"{cur_dir}/input") as f:
    for line in f:
        command, xmin, xmax, ymin, ymax, zmin, zmax = parse_command(line)

        # xmin, xmax = shift_and_normalize_extents(xmin, xmax)
        # ymin, ymax = shift_and_normalize_extents(ymin, ymax)
        # zmin, zmax = shift_and_normalize_extents(zmin, zmax)

        print(f"{xmin}, {xmax}, {ymin}, {ymax}, {zmin}, {zmax}")
        # print(reactor[xmin : xmax + 1, ymin : ymax + 1, zmin : zmax + 1])

        if command == "on":
            cand_on_blocks = [Block(xmin, xmax, ymin, ymax, zmin, zmax)]

            for on_block in on_blocks:
                next_cand_on_blocks = []
                for cand in cand_on_blocks:
                    inter = on_block.intersection(cand)
                    if inter.num_cubes() == 0:
                        next_cand_on_blocks.append(cand)
                    else:
                        next_cand_on_blocks += cand.subtract(inter)
                cand_on_blocks = next_cand_on_blocks

            on_blocks += cand_on_blocks

        elif command == "off":
            off_block = Block(xmin, xmax, ymin, ymax, zmin, zmax)
            updated_on_blocks = []
            for on_block in on_blocks:
                inter = on_block.intersection(off_block)
                if inter.num_cubes() == 0:
                    updated_on_blocks.append(on_block)
                else:
                    updated_on_blocks += on_block.subtract(inter)
            on_blocks = updated_on_blocks
        else:
            raise Exception("Unknown command")
        # print(reactor[xmin : xmax + 1, ymin : ymax + 1, zmin : zmax + 1])
        # for x in on_blocks:
        #     print(x)
        print(sum([x.num_cubes() for x in on_blocks]))

print(sum([x.num_cubes() for x in on_blocks]))

print(sum([x.intersection(init_block).num_cubes() for x in on_blocks]))
