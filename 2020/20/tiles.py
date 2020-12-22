def rotate_grid_left(grid):
    new_grid = []
    gridx = len(grid[0])
    gridy = len(grid)
    for _ in range(gridy):
        new_grid.append([" "] * gridx)
    
    for i in range(gridy):
        for j in range(gridx):
            new_grid[gridy - 1 - j][i] = grid[i][j]
            
    return new_grid


def mirror_grid(grid):
    new_grid = []
    gridx = len(grid[0])
    gridy = len(grid)
    for _ in range(gridy):
        new_grid.append([" "] * gridx)
    
    for i in range(gridy):
        for j in range(gridx):
            new_grid[i][gridx - j - 1] = grid[i][j]
            
    return new_grid


class Tile:
    
    def __init__(self, id, layout):
        
        self.id = id
        self.layout = layout
        self.shape_y = len(self.layout)
        self.shape_x = 0
        if self.shape_y > 0:
            self.shape_x = len(self.layout[0])
            
        self.edges = []
        # Construct edges
        self.edges.append(list(layout[0]))
        self.edges.append([x[self.shape_x - 1] for x in layout])
        self.edges.append(list(layout[self.shape_y - 1]))
        self.edges.append([x[0] for x in layout])
        
        self.possible_neighbors = [[], [], [], []]
        
    def determine_possible_neighbors(self, tiles):
        self.possible_neighbors = [[], [], [], []]
        
        for other_tile in tiles:
            if other_tile.id == self.id:
                continue
            for i, edge in enumerate(self.edges):
                for j, other_edge in enumerate(other_tile.edges):
                    if "".join(edge) == "".join(other_edge) or "".join(edge) == "".join(reversed(other_edge)):
                        self.possible_neighbors[i].append((other_tile.id, j))
                        
    def number_of_edges_possible_to_connect(self):
        val = 0
        for x in self.possible_neighbors:
            if len(x) != 0:
                val += 1
        return val
    
    def rotate_to_orientation(self, orientation):
        mirrored = ((orientation[0] - orientation[1]) % 4 == 1)
        # mirrored = orientation[0] > orientation[1]
        # if orientation[0] == 3 or orientation[1] == 3:
        #     mirrored = orientation[1] > orientation[2]
            
        for _ in range(orientation[0]):
            self.layout = rotate_grid_left(self.layout)
            self.edges = self.edges[1:] + self.edges[:1]
            self.possible_neighbors = self.possible_neighbors[1:] + self.possible_neighbors[:1]
            
        if mirrored:
            self.layout = mirror_grid(self.layout)
            self.edges = [self.edges[0], self.edges[3], self.edges[2], self.edges[1]]
            self.possible_neighbors = [self.possible_neighbors[0], self.possible_neighbors[3], self.possible_neighbors[2], self.possible_neighbors[1]]
            
    def layout_without_borders(self):
        return [[x for x in row[1:-1]] for row in self.layout[1:-1]]
                        
    def print_neighbor_candidates(self):
        print(f"ID: {self.id}")
        print(f"0: {self.possible_neighbors[0]}")
        print(f"1: {self.possible_neighbors[1]}")
        print(f"2: {self.possible_neighbors[2]}")
        print(f"3: {self.possible_neighbors[3]}")
        
    def print_tile(self):
        print(f"ID: {self.id}")
        for line in self.layout:
            print("".join(line))
        
