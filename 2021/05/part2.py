import os
from typing import List, Tuple


def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    ep_1 = line.split(" -> ")[0]
    ep_2 = line.split(" -> ")[1]

    return tuple([int(x) for x in ep_1.split(",")]), tuple(
        [int(x) for x in ep_2.split(",")]
    )


def expand_vertical_line(
    ep1: Tuple[int, int], ep2: Tuple[int, int]
) -> List[Tuple[int, int]]:
    x = ep1[0]
    start = min(ep1[1], ep2[1])
    end = max(ep1[1], ep2[1])
    return [(x, y) for y in range(start, end + 1, 1)]


def expand_horizontal_line(
    ep1: Tuple[int, int], ep2: Tuple[int, int]
) -> List[Tuple[int, int]]:
    y = ep1[1]
    start = min(ep1[0], ep2[0])
    end = max(ep1[0], ep2[0])
    return [(x, y) for x in range(start, end + 1, 1)]


def expand_diagonal_line(
    ep1: Tuple[int, int], ep2: Tuple[int, int]
) -> List[Tuple[int, int]]:
    # Guaranteed to be integer so we can use integer division
    slope = (ep2[1] - ep1[1]) // (ep2[0] - ep1[0])
    step_size = 1
    if ep2[0] < ep1[0]:
        step_size = -1
    return [
        (x, ep1[1] + slope * (x - ep1[0]))
        for x in range(ep1[0], ep2[0] + step_size, step_size)
    ]


def expand_line(ep1: Tuple[int, int], ep2: Tuple[int, int]) -> List[Tuple[int, int]]:
    if ep1[0] == ep2[0]:
        return expand_vertical_line(ep1, ep2)
    elif ep1[1] == ep2[1]:
        return expand_horizontal_line(ep1, ep2)
    return expand_diagonal_line(ep1, ep2)


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    lines = [parse_line(x) for x in f]

points_count = {}

for line in lines:
    points = expand_line(line[0], line[1])
    for point in points:
        if point in points_count:
            points_count[point] += 1
        else:
            points_count[point] = 1

print(len([x for x in points_count if points_count[x] > 1]))