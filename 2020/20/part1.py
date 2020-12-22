import os

import tiles


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
        
print(f"The product of the corner IDs is {corner_val}")
