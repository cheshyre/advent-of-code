import os
from typing import List, Sequence


def is_small_cave(node: str) -> bool:
    return node.islower()


class Graph:
    def __init__(self, paths: Sequence[str]) -> None:
        self.nodes = list(
            set(
                list({path.split("-")[1] for path in paths})
                + list({path.split("-")[0] for path in paths})
            )
        )
        self.node_index_lookup = {x: i for i, x in enumerate(self.nodes)}
        self.matrix = [[0 for _ in self.nodes] for _ in self.nodes]

        for path in paths:
            a, b = tuple(path.split("-"))
            a_i = self.node_index_lookup[a]
            b_i = self.node_index_lookup[b]

            self.matrix[a_i][b_i] = 1
            self.matrix[b_i][a_i] = 1

    def get_node_neighbors(self, node) -> List[str]:
        n_i = self.node_index_lookup[node]
        return [self.nodes[i] for i, x in enumerate(self.matrix[n_i]) if x == 1]


class Path:
    def __init__(self, graph: Graph, nodes: Sequence[str]) -> None:
        self.graph = graph
        self.nodes = list(nodes)
        self.small_caves_list = [x for x in nodes if is_small_cave(x)]
        self.small_caves = {x for x in nodes if is_small_cave(x)}
        self.blocked = set(["start"])
        if len(self.small_caves_list) != len(self.small_caves):
            self.blocked = self.small_caves

    def clone_and_set_new_node(self, node):
        return Path(self.graph, self.nodes + [node])

    def last_cave(self):
        return self.nodes[-1]

    def get_neighbors(self):
        return self.graph.get_node_neighbors(self.last_cave())

    def at_end(self):
        return self.last_cave() == "end" or len(self.get_neighbors()) == 0

    def set_next_node(self, node):
        self.nodes.append(node)
        if is_small_cave(node):
            self.blocked.add(node)

    def __repr__(self) -> str:
        return ",".join(self.nodes)


cur_dir = os.path.dirname(os.path.abspath(__file__))


with open(f"{cur_dir}/input") as f:
    paths = [x.strip() for x in f]

graph = Graph(paths)

print(graph.nodes)

inc_paths = [Path(graph, ["start"])]

comp_paths = []
while len(inc_paths) > 0:
    new_paths = []

    for path in inc_paths:
        neighbors = path.get_neighbors()
        new_paths += [
            path.clone_and_set_new_node(x) for x in neighbors if x not in path.blocked
        ]

    comp_paths += [x for x in new_paths if x.at_end() and x.last_cave() == "end"]
    inc_paths = [x for x in new_paths if not x.at_end()]

for x in comp_paths:
    print(x)

print(len(comp_paths))
