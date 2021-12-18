import os
from typing import Any, List, Tuple


cur_dir = os.path.dirname(os.path.abspath(__file__))


def parse_line_to_pair(line: str) -> Tuple[List[int], List[int]]:
    numbers = []
    depths = []

    depth = 0
    for x in line.strip():
        if x == "[":
            depth += 1
        elif x == "]":
            depth -= 1
        elif x == ",":
            pass
        else:
            numbers.append(int(x))
            depths.append(depth)

    return numbers, depths


def explode_pair(
    pair: Tuple[List[int], List[int]]
) -> Tuple[Tuple[List[int], List[int]], bool]:

    n, d = pair

    for i, x in enumerate(d):
        if x == 5:
            left = n[i]
            right = n[i + 1]

            if i != 0:
                n[i - 1] += left
            if i + 1 != len(d) - 1:
                n[i + 2] += right

            new_d = d[:i] + [4] + d[i + 2 :]
            new_n = n[:i] + [0] + n[i + 2 :]

            return (new_n, new_d), True

    return (n, d), False


def split_pair(
    pair: Tuple[List[int], List[int]]
) -> Tuple[Tuple[List[int], List[int]], bool]:

    n, d = pair

    for i, x in enumerate(n):
        if x > 9:
            old_depth = d[i]

            new_n = n[:i] + [x // 2, x - x // 2] + n[i + 1 :]
            new_d = d[:i] + [old_depth + 1, old_depth + 1] + d[i + 1 :]

            return (new_n, new_d), True

    return (n, d), False


def reduce_pair(pair: Tuple[List[int], List[int]]) -> Tuple[List[int], List[int]]:

    modified = True

    while modified:
        modified = False

        pair, explode_mod = explode_pair(pair)

        modified = modified or explode_mod

        if not modified:

            pair, split_mod = split_pair(pair)
            modified = modified or split_mod

    return pair


def add_pairs(
    pair1: Tuple[List[int], List[int]], pair2: Tuple[List[int], List[int]]
) -> Tuple[List[int], List[int]]:
    n1, d1 = pair1
    n2, d2 = pair2

    new_n = n1 + n2
    new_d = [x + 1 for x in d1 + d2]

    return new_n, new_d


def recreate_pair(pair: Tuple[List[int], List[int]]) -> List[Any]:
    n, d = pair
    new_n, new_d = list(n), list(d)

    while len(new_n) != 2:
        for i in range(len(new_n)):
            if new_d[i] == new_d[i + 1]:
                new_n = new_n[:i] + [[new_n[i], new_n[i + 1]]] + new_n[i + 2 :]
                new_d = new_d[:i] + [new_d[i] - 1] + new_d[i + 2 :]

                break

    return new_n


def get_pair_magnitude(pair) -> int:
    try:
        left = pair[0]
        right = pair[1]

        return 3 * get_pair_magnitude(left) + 2 * get_pair_magnitude(right)
    except TypeError:
        return pair


with open(f"{cur_dir}/input") as f:
    lines = [x.strip() for x in f]

pairs = [parse_line_to_pair(line) for line in lines]
pair_sums_mags = [
    get_pair_magnitude(recreate_pair(reduce_pair(add_pairs(x, y))))
    for x in pairs
    for y in pairs
]

print(max(pair_sums_mags))
