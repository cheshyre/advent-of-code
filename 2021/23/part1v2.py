import os
from typing import List, Mapping, Optional, Tuple

cur_dir = os.path.dirname(os.path.abspath(__file__))


AMPHIPOD_COSTS = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

HALLWAY_Y = 1
HOLE_X = [3, 5, 7, 9]

AMPHIPOD_HOLE_X = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9,
}


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def as_tuple(self) -> Tuple[int, int]:
        return self.x, self.y

    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Point):
            return NotImplemented
        return self.as_tuple() == __o.as_tuple()

    def path_to_horiz(self, end_pt: "Point") -> List["Point"]:
        if self.y != end_pt.y:
            raise Exception()
        direction = 1
        if end_pt.x < self.x:
            direction = -1

        pts = [
            Point(x, self.y)
            for x in range(self.x + direction, end_pt.x + direction, direction)
        ]
        return pts

    def path_to_vert(self, end_pt: "Point") -> List["Point"]:
        if self.x != end_pt.x:
            raise Exception()
        direction = 1
        if end_pt.y < self.y:
            direction = -1

        pts = [
            Point(self.x, y)
            for y in range(self.y + direction, end_pt.y + direction, direction)
        ]
        return pts

    def path_to(self, end_pt: "Point") -> List["Point"]:
        # if end_pt.y < self.y:
        #     interm = Point(self.x, end_pt.y)
        #     return self.path_to_vert(interm) + interm.path_to_horiz(end_pt)
        # else:
        #     interm = Point(end_pt.x, self.y)
        #     return self.path_to_horiz(interm) + interm.path_to_vert(end_pt)
        if self.x == end_pt.x:
            return self.path_to_vert(end_pt)
        interm1 = Point(self.x, HALLWAY_Y)
        interm2 = Point(end_pt.x, HALLWAY_Y)

        return (
            self.path_to_vert(interm1)
            + interm1.path_to_horiz(interm2)
            + interm2.path_to_vert(end_pt)
        )

    def __repr__(self) -> str:
        return str(self.as_tuple())


def generate_open_points(positions: Mapping[Point, str]) -> List[Point]:
    return [x for x in positions if positions[x] == "."]


def generate_amphipod_positions(
    positions: Mapping[Point, str]
) -> Mapping[str, Tuple[Point, Point]]:
    amphipod_positions = {}
    for x in AMPHIPOD_COSTS:
        amphipod_positions[x] = []

    for x in positions:
        if positions[x] in AMPHIPOD_COSTS:
            amphipod_positions[positions[x]].append(x)

    return {
        x: (amphipod_positions[x][0], amphipod_positions[x][1])
        for x in amphipod_positions
    }


def compute_heuristic_single_type(
    positions: Mapping[Point, str], amphipod_type: str, pt1: Point, pt2: Point
) -> int:
    target = Point(AMPHIPOD_HOLE_X[amphipod_type], HALLWAY_Y + 2)
    heuristic_dist = len(pt1.path_to(target)) + len(pt2.path_to(target))
    pre_target = Point(AMPHIPOD_HOLE_X[amphipod_type], HALLWAY_Y + 1)
    if pt1 == pre_target or pt2 == pre_target:
        if positions[target] != amphipod_type:
            heuristic_dist += 4

    return AMPHIPOD_COSTS[amphipod_type] * (heuristic_dist - 1)


def compute_heuristic(
    positions: Mapping[Point, str],
    amphipod_positions: Mapping[str, Tuple[Point, Point]],
) -> int:
    return sum(
        [
            compute_heuristic_single_type(
                positions, x, amphipod_positions[x][0], amphipod_positions[x][1]
            )
            for x in amphipod_positions
        ]
    )


def generate_unique_id(positions: Mapping[Point, str]) -> str:
    hallway_pts = [x.x for x in positions if x.y == HALLWAY_Y]
    hallway_min_x = min(hallway_pts)
    hallway_max_x = max(hallway_pts)

    identifier = ""

    for x in range(hallway_min_x, hallway_max_x + 1):
        identifier += positions[Point(x, HALLWAY_Y)]

    for x in HOLE_X:
        for y in [HALLWAY_Y + 1, HALLWAY_Y + 2]:
            identifier += positions[Point(x, y)]

    return identifier


class BoardState:
    def __init__(
        self,
        positions: Mapping[Point, str],
        cost: int = 0,
        parent: Optional["BoardState"] = None,
    ) -> None:
        self.parent = parent
        self.positions = positions
        self.cost = cost
        self.open_points = generate_open_points(self.positions)
        self.amphipod_positions = generate_amphipod_positions(self.positions)
        self.heuristic = compute_heuristic(self.positions, self.amphipod_positions)
        self.uid = generate_unique_id(self.positions)

    def estimated_cost(self) -> int:
        return self.cost + self.heuristic

    def __hash__(self) -> int:
        return hash(self.uid)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, BoardState):
            return NotImplemented
        return self.uid == __o.uid

    def is_valid_destination(
        self, amphipod_type: str, start: Point, end: Point
    ) -> bool:
        if end.y > HALLWAY_Y and end.x != AMPHIPOD_HOLE_X[amphipod_type]:
            return False
        if end.x in HOLE_X and end.y == HALLWAY_Y:
            return False
        if (
            end.y == HALLWAY_Y + 1
            and self.positions[Point(end.x, end.y + 1)] != amphipod_type
        ):
            return False
        if start.y == HALLWAY_Y and end.y == HALLWAY_Y:
            return False
        if (
            start.y == HALLWAY_Y + 1
            and self.positions[Point(start.x, start.y + 1)] == amphipod_type
        ):
            return False
        return True

    def is_path_open(self, start: Point, end: Point) -> bool:
        path = start.path_to(end)

        for x in path:
            if self.positions[x] != ".":
                return False

        return True

    def generate_next_valid_boards(self) -> List["BoardState"]:
        next_boards = []

        for x in self.amphipod_positions:
            for start_pt in self.amphipod_positions[x]:
                for end_pt in self.open_points:

                    # print(f"Move {start_pt} to {end_pt}")

                    if self.is_valid_destination(
                        self.positions[start_pt], start_pt, end_pt
                    ) and self.is_path_open(start_pt, end_pt):
                        new_positions = {x: self.positions[x] for x in self.positions}
                        new_positions[end_pt] = self.positions[start_pt]
                        new_positions[start_pt] = "."
                        path_len = len(start_pt.path_to(end_pt))
                        cost = (
                            self.cost
                            + AMPHIPOD_COSTS[self.positions[start_pt]] * path_len
                        )

                        next_boards.append(BoardState(new_positions, cost, self))

        return next_boards

    def visualize(self) -> None:
        for y in range(HALLWAY_Y + 4):
            for x in range(14):
                if Point(x, y) in self.positions:
                    print(self.positions[Point(x, y)], end="")
                else:
                    print("#", end="")
            print("")


pts = {}
with open(f"{cur_dir}/input") as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.rstrip()):
            if c in [".", "A", "B", "C", "D"]:
                pts[Point(x, y)] = c

print(pts)
state = BoardState(pts)
state.visualize()

states = [state]
visited_states = set()
solution_found = len([x for x in states if x.heuristic == 0]) != 0
while not solution_found:
    state = states[0]
    print(state.estimated_cost())
    state.visualize()
    states = states[1:]

    visited_states.add(state)

    next_states = state.generate_next_valid_boards()
    next_states = [x for x in next_states if x not in visited_states]

    states += next_states

    states.sort(key=lambda x: x.estimated_cost())
    solution_found = len([x for x in states if x.heuristic == 0]) != 0
    if solution_found:
        solution = [x for x in states if x.heuristic == 0][0]

    states = [x for x in states if x not in visited_states]

    # for x in states:
    #     print(x.estimated_cost())
    #     x.visualize()

print(solution.cost)

path = []
while solution is not None:
    path.append(solution)
    solution = solution.parent
print("Full path")
for x in reversed(path):
    print(x.cost)
    x.visualize()
