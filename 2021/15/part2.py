import os


cur_dir = os.path.dirname(os.path.abspath(__file__))

UNDETERMINED = 99999999

NEIGHBORS = [
    (x, y)
    for x in [-1, 0, 1]
    for y in [-1, 0, 1]
    if (x != 0 or y != 0) and (abs(x) + abs(y) == 1)
]


def get_neighbors(x, y, max_x, max_y):
    return [
        (x + dx, y + dy)
        for dx, dy in NEIGHBORS
        if x + dx <= max_x and x + dx >= 0 and y + dy <= max_y and y + dy >= 0
    ]


def dict_diff(a, b):
    if len(a) != len(b):
        return False
    for x in a:
        if x not in b:
            return False
        if a[x] != b[x]:
            return False
    return True


class Graph:
    def __init__(self, local_costs, max_x, max_y, end) -> None:
        self.local_costs = {x: local_costs[x] for x in local_costs}
        self.costs = {end: self.local_costs[end]}
        self.max_x = max_x
        self.max_y = max_y
        self.end = end

    def iterate_cost_graph(self) -> bool:
        new_costs = {self.end: self.local_costs[self.end]}
        for x, y in self.local_costs:
            if (x, y) == self.end:
                continue
            neighbors = get_neighbors(x, y, self.max_x, self.max_y)
            cost = self.local_costs[(x, y)] + min(
                [
                    self.costs[(xn, yn)] if (xn, yn) in self.costs else UNDETERMINED
                    for xn, yn in neighbors
                ]
            )
            new_costs[(x, y)] = cost
        stable = dict_diff(new_costs, self.costs)

        self.costs = new_costs

        return stable


with open(f"{cur_dir}/input") as f:
    grid = [[int(x) for x in line.strip()] for line in f]

max_x = len(grid)
max_y = len(grid[0])

major_grids = 5

local_costs = {(x, y): grid[x][y] for x in range(max_x) for y in range(max_y)}

cost = list(range(1, 10))

new_local_costs = {x: local_costs[x] for x in local_costs}
for maj_x in range(major_grids):
    for maj_y in range(major_grids):
        if (maj_x, maj_y) == (0, 0):
            continue
        dist = maj_x + maj_y

        for x, y in local_costs:
            newx = maj_x * max_x + x
            newy = maj_y * max_y + y

            new_local_costs[(newx, newy)] = cost[
                (local_costs[(x, y)] - 1 + dist) % len(cost)
            ]

local_costs = new_local_costs

graph = Graph(
    local_costs,
    major_grids * max_x - 1,
    major_grids * max_y - 1,
    (major_grids * max_x - 1, major_grids * max_y - 1),
)

target = (0, 0)
while True:
    stable = graph.iterate_cost_graph()

    print(graph.costs[target] - graph.local_costs[target])

    if stable:
        break
