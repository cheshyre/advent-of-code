import os
from typing import List, Sequence, Tuple

import numpy as np


cur_dir = os.path.dirname(os.path.abspath(__file__))


class Rotation:
    def __init__(self, matrix: np.ndarray) -> None:
        self.matrix = matrix


ROTATIONS = {
    "x_0": Rotation(
        np.array(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ]
        )
    ),
    "x_90": Rotation(
        np.array(
            [
                [1, 0, 0],
                [0, 0, -1],
                [0, 1, 0],
            ]
        )
    ),
    "x_180": Rotation(
        np.array(
            [
                [1, 0, 0],
                [0, -1, 0],
                [0, 0, -1],
            ]
        )
    ),
    "x_270": Rotation(
        np.array(
            [
                [1, 0, 0],
                [0, 0, 1],
                [0, -1, 0],
            ]
        )
    ),
    "y_0": Rotation(
        np.array(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ]
        )
    ),
    "y_90": Rotation(
        np.array(
            [
                [0, 0, 1],
                [0, 1, 0],
                [-1, 0, 0],
            ]
        )
    ),
    "y_180": Rotation(
        np.array(
            [
                [-1, 0, 0],
                [0, 1, 0],
                [0, 0, -1],
            ]
        )
    ),
    "y_270": Rotation(
        np.array(
            [
                [0, 0, -1],
                [0, 1, 0],
                [1, 0, 0],
            ]
        )
    ),
    "z_0": Rotation(
        np.array(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ]
        )
    ),
    "z_90": Rotation(
        np.array(
            [
                [0, -1, 0],
                [1, 0, 0],
                [0, 0, 1],
            ]
        )
    ),
    "z_180": Rotation(
        np.array(
            [
                [-1, 0, 0],
                [0, -1, 0],
                [0, 0, 1],
            ]
        )
    ),
    "z_270": Rotation(
        np.array(
            [
                [0, 1, 0],
                [-1, 0, 0],
                [0, 0, 1],
            ]
        )
    ),
}


class Translation:
    def __init__(self, offset: np.ndarray) -> None:
        self.shift = offset

    @classmethod
    def from_xyz(cls, x: int, y: int, z: int) -> "Point":
        return cls(np.array([x, y, z]))

    def __repr__(self) -> str:
        return str((self.shift[0], self.shift[1], self.shift[0]))

    def __add__(self, trans: "Translation") -> "Translation":
        return Translation(self.shift + trans.shift)

    def as_tuple(self) -> Tuple[int, int, int]:
        return self.shift[0], self.shift[1], self.shift[2]

    def __eq__(self, o: "Point") -> bool:
        return self.as_tuple() == o.as_tuple()

    def __repr__(self) -> str:
        return str(self.as_tuple())

    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def as_point(self) -> "Point":
        return Point(self.shift)

    def is_detectable(self) -> bool:
        x, y, z = self.as_tuple()
        return abs(x) <= 1000 and abs(y) <= 1000 and abs(z) <= 1000


class Point:
    def __init__(self, pt: np.ndarray) -> None:
        self.pt = pt

    @classmethod
    def from_xyz(cls, x: int, y: int, z: int) -> "Point":
        return cls(np.array([x, y, z]))

    def rotate(self, rot: Rotation) -> "Point":
        return Point(rot.matrix @ self.pt)

    def translate(self, trans: Translation) -> "Point":
        return Point(self.pt + trans.shift)

    def __sub__(self, pt: "Point") -> Translation:
        return Translation(self.pt - pt.pt)

    def as_tuple(self) -> Tuple[int, int, int]:
        return self.pt[0], self.pt[1], self.pt[2]

    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def __eq__(self, o: "Point") -> bool:
        return self.as_tuple() == o.as_tuple()

    def __repr__(self) -> str:
        return str(self.as_tuple())


def parse_file(lines: Sequence[str]) -> List[List[Point]]:
    ret_val = []

    cur_scanner = []
    for line in lines:
        line = line.strip()

        if "---" in line:
            continue

        if line == "":
            ret_val.append(cur_scanner)
            cur_scanner = []
        else:
            x, y, z = tuple([int(x) for x in line.split(",")])
            cur_scanner.append(Point.from_xyz(x, y, z))

    if len(cur_scanner) != 0:
        ret_val.append(cur_scanner)
        cur_scanner = []

    return ret_val


def find_possible_overlap(
    cand: Sequence[Point], ref: Sequence[Point], min_count: int, ref_origin: Point
) -> Tuple[bool, List[Point], Translation]:
    origin = Point.from_xyz(0, 0, 0)

    ref_set = set(ref)

    for x in [0, 90, 180, 270]:
        rot_x = ROTATIONS[f"x_{x}"]
        for y in [0, 90, 180, 270]:
            rot_y = ROTATIONS[f"y_{y}"]
            rot_yx = Rotation(rot_y.matrix @ rot_x.matrix)
            for z in [0, 90, 180, 270]:
                print(f"Rotating {x}, {y}, {z} degrees around x, y, z")
                rot_z = ROTATIONS[f"z_{z}"]
                rot_zyx = Rotation(rot_z.matrix @ rot_yx.matrix)

                rotated_cand = [pt.rotate(rot_zyx) for pt in cand]

                for cand_anchor in rotated_cand:
                    for ref_anchor in ref:
                        trans = ref_anchor - cand_anchor

                        rot_trans_cand = [pt.translate(trans) for pt in rotated_cand]

                        shared_pts = [
                            cand_pt for cand_pt in rot_trans_cand if cand_pt in ref_set
                        ]

                        # detectable_nonshared_pts = [
                        #     ref_pt
                        #     for ref_pt in ref
                        #     if ref_pt not in rot_trans_cand
                        #     and (ref_pt - origin.translate(trans)).is_detectable()
                        # ] + [
                        #     cand_pt
                        #     for cand_pt in rot_trans_cand
                        #     if cand_pt not in ref and (cand_pt - origin).is_detectable()
                        # ]

                        if len(shared_pts) >= min_count:

                            shared_pts_set = set(shared_pts)

                            detectable_nonshared_pts = [
                                ref_pt
                                for ref_pt in ref
                                if ref_pt not in shared_pts_set
                                and (ref_pt - origin.translate(trans)).is_detectable()
                            ] + [
                                cand_pt
                                for cand_pt in rot_trans_cand
                                if cand_pt not in shared_pts_set
                                and (cand_pt - ref_origin).is_detectable()
                            ]

                            if len(detectable_nonshared_pts) == 0:
                                for val in shared_pts:
                                    print(val)
                                return True, rot_trans_cand, trans

    return False, [], Translation.from_xyz(0, 0, 0)


with open(f"{cur_dir}/input") as f:
    lines = [line.strip() for line in f]

beacons = parse_file(lines)

for x in beacons:
    print(x)

shifted_beacons = [beacons[0]]
scanners_numbers = [0]
scanner_offsets = [Translation(np.array([0, 0, 0]))]

checked_combinations = set()

while len(shifted_beacons) != len(beacons):

    for i, x in enumerate(scanners_numbers):

        for y in range(len(beacons)):

            if y in scanners_numbers:
                continue
            if (x, y) in checked_combinations:
                continue

            print(f"Scanner {x} vs {y}")

            checked_combinations.add((x, y))

            found, shifted, offset = find_possible_overlap(
                beacons[y], shifted_beacons[i], 12, scanner_offsets[i].as_point()
            )

            if found:
                print(f"Shifted scanner {y}")
                for val in shifted:
                    print(val)
                shifted_beacons.append(shifted)
                scanners_numbers.append(y)
                scanner_offsets.append(offset)

print(scanners_numbers)
print(scanner_offsets)

final_beacons = []
for beacons in shifted_beacons:
    final_beacons += beacons
print(len(set(final_beacons)))

with open(f"{cur_dir}/output", "w") as f:
    for x in set(final_beacons):
        f.write(f"{x.pt[0]},{x.pt[1]},{x.pt[2]}\n")
