import os

import tiles
import sea_monster


cur_dir = os.path.dirname(os.path.abspath(__file__))

mytiles = []
with open(f"{cur_dir}/input") as f:
    cur_line = f.readline()
    while cur_line != "":
        tile_id = int(cur_line.strip().split()[1][:-1])
        tile_layout = []
        cur_line = f.readline()
        while cur_line.strip() != "":
            tile_layout.append([x for x in cur_line.strip()])
            cur_line = f.readline()
    
        mytiles.append(tiles.Tile(tile_id, tile_layout))
        cur_line = f.readline()
    
corners = []
tile_lookup = {}
for tile in mytiles:
    tile.determine_possible_neighbors(mytiles)
    # tile.print_neighbor_candidates()
    if tile.number_of_edges_possible_to_connect() == 2:
        corners.append(tile.id)
    tile_lookup[tile.id] = tile
        
corner_val = 1
for x in corners:
    corner_val *= x

tile_grid = [[]]

cur_id = corners[0]
cur_tile = tile_lookup[cur_id]
cur_tile.print_neighbor_candidates()
# cur_tile.rotate_to_orientation((2, 1, 0, 3))
cur_tile.rotate_to_orientation((1, 2, 3, 0))
tile_grid[0].append(cur_id)

# Fill out top row
cur_id = cur_tile.possible_neighbors[1][0][0]
edge_id = cur_tile.possible_neighbors[1][0][1]
cur_tile = tile_lookup[cur_id]
while cur_id not in corners:
    for i in range(4):
        if len(cur_tile.possible_neighbors[i]) == 0:
            empty_edge_id = i
            break
    if empty_edge_id == (edge_id + 1) % 4:
        orientation = tuple([x % 4 for x in range(empty_edge_id, empty_edge_id + 3)] + [edge_id])
    else:
        orientation = tuple([x % 4 for x in range(empty_edge_id, empty_edge_id - 3, -1)] + [edge_id])
    cur_tile.rotate_to_orientation(orientation)
    tile_grid[0].append(cur_id)
    cur_id = cur_tile.possible_neighbors[1][0][0]
    edge_id = cur_tile.possible_neighbors[1][0][1]
    cur_tile = tile_lookup[cur_id]

for i in range(4):
    if len(cur_tile.possible_neighbors[i]) == 0 and (i - edge_id) % 2 != 0:
        empty_edge_id = i
        break
if empty_edge_id == (edge_id + 1) % 4:
    orientation = tuple([x % 4 for x in range(empty_edge_id, empty_edge_id + 3)] + [edge_id])
else:
    orientation = tuple([x % 4 for x in range(empty_edge_id, empty_edge_id - 3, -1)] + [edge_id])
cur_tile.rotate_to_orientation(orientation)
tile_grid[0].append(cur_id)

# Fill out left side
cur_id = tile_grid[0][0]
cur_tile = tile_lookup[cur_id]
cur_id = cur_tile.possible_neighbors[2][0][0]
edge_id = cur_tile.possible_neighbors[2][0][1]
cur_tile = tile_lookup[cur_id]

while cur_id not in corners:
    for i in range(4):
        if len(cur_tile.possible_neighbors[i]) == 0:
            empty_edge_id = i
            break
    if empty_edge_id == (edge_id - 1) % 4:
        orientation = tuple([x % 4 for x in range(edge_id, edge_id + 3)] + [empty_edge_id])
    else:
        orientation = tuple([x % 4 for x in range(edge_id, edge_id - 3, -1)] + [empty_edge_id])
    cur_tile.rotate_to_orientation(orientation)
    tile_grid.append([cur_id])
    cur_id = cur_tile.possible_neighbors[2][0][0]
    edge_id = cur_tile.possible_neighbors[2][0][1]
    cur_tile = tile_lookup[cur_id]

for i in range(4):
    if len(cur_tile.possible_neighbors[i]) == 0 and (i - edge_id) % 2 != 0:
        empty_edge_id = i
        break
if empty_edge_id == (edge_id - 1) % 4:
    orientation = tuple([x % 4 for x in range(edge_id, edge_id + 3)] + [empty_edge_id])
else:
    orientation = tuple([x % 4 for x in range(edge_id, edge_id - 3, -1)] + [empty_edge_id])
cur_tile.rotate_to_orientation(orientation)
tile_grid.append([cur_id])

dimx = len(tile_grid[0])
dimy = len(tile_grid)

for y in range(1, dimy):
    for x in range(1, dimx):
        left_tile_id = tile_grid[y][x - 1]
        top_tile_id = tile_grid[y - 1][x]
        left_tile = tile_lookup[left_tile_id]
        top_tile = tile_lookup[top_tile_id]
        cur_id = left_tile.possible_neighbors[1][0][0]
        if cur_id != top_tile.possible_neighbors[2][0][0]:
            print("Warning: IDs are inconsistent in reconstruction")
            exit(-1)
        cur_tile = tile_lookup[cur_id]
        left_edge_id = left_tile.possible_neighbors[1][0][1]
        top_edge_id = top_tile.possible_neighbors[2][0][1]
        if top_edge_id == left_edge_id + 1 % 4:
            orientation = tuple([x % 4 for x in range(top_edge_id, top_edge_id + 3)] + [left_edge_id])
        else:
            orientation = tuple([x % 4 for x in range(top_edge_id, top_edge_id - 3, -1)] + [left_edge_id])
        # cur_tile.print_neighbor_candidates()
        # print(orientation)
        cur_tile.rotate_to_orientation(orientation)
        tile_grid[y].append(cur_id)
# cur_tile.print_neighbor_candidates()
        
for row in tile_grid:
    for tile_id in row:
        this_tile = tile_lookup[tile_id]
        # this_tile.print_tile()

imagegrid = []
for row in tile_grid:
    tile_id = row[0]
    this_tile = tile_lookup[tile_id]
    layout = this_tile.layout_without_borders()
    for x in layout:
        imagegrid.append(x)

for i, row in enumerate(tile_grid):
    for tile_id in row[1:]:
        this_tile = tile_lookup[tile_id]
        layout = this_tile.layout_without_borders()
        for j, x in enumerate(layout):
            imagegrid[i * len(layout) + j] += x

print("Full image")
for x in imagegrid:
    print("".join(x))
    
for i in range(8):
    sm_found, imagegrid = sea_monster.mark_sea_monsters(imagegrid)
    if sm_found:
        break
    if i % 4 == 0:
        imagegrid = tiles.mirror_grid(imagegrid)
    else:
        imagegrid = tiles.rotate_grid_left(imagegrid)
        
print("Image with marked sea monsters")
count_waves = 0
for x in imagegrid:
    count_waves += x.count("#")
    print("".join(x))

print(f"There are {count_waves} waves.")
    