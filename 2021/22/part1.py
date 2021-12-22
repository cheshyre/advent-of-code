import os
from typing import Tuple

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


with open(f"{cur_dir}/input") as f:
    for line in f:
        command, xmin, xmax, ymin, ymax, zmin, zmax = parse_command(line)

        xmin, xmax = shift_and_normalize_extents(xmin, xmax)
        ymin, ymax = shift_and_normalize_extents(ymin, ymax)
        zmin, zmax = shift_and_normalize_extents(zmin, zmax)

        print(f"{xmin}, {xmax}, {ymin}, {ymax}, {zmin}, {zmax}")
        # print(reactor[xmin : xmax + 1, ymin : ymax + 1, zmin : zmax + 1])

        if command == "on":
            reactor[xmin : xmax + 1, ymin : ymax + 1, zmin : zmax + 1] = 1
        elif command == "off":
            reactor[xmin : xmax + 1, ymin : ymax + 1, zmin : zmax + 1] = 0
        else:
            raise Exception("Unknown command")
        # print(reactor[xmin : xmax + 1, ymin : ymax + 1, zmin : zmax + 1])
        print(np.sum(reactor))

print(np.sum(reactor))
