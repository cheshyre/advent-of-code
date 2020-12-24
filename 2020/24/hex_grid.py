def parse_instructions(instr_str):
    instr_str = instr_str.strip()
    instructions = []
    while instr_str != "":
        instr, instr_str = parse_single_instruction(instr_str)
        instructions.append(instr)
    
    return instructions
        
    
def parse_single_instruction(instr_str):
    if instr_str[0] in ["n", "s"]:
        return instr_str[:2], instr_str[2:]
    return instr_str[:1], instr_str[1:]


def apply_instruction_to_point(point, instr):
    instr_offsets = {
        "w": (-1, 0),
        "e": (1, 0),
        "sw": (-1, -1),
        "se": (0, -1),
        "nw": (0, 1),
        "ne": (1, 1),
    }
    x, y = point
    xoff, yoff = instr_offsets[instr]
    return x + xoff, y + yoff
    

def get_neighbors(point):
    offsets = [
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, -1),
        (0, 1),
        (1, 1),
    ]
    x, y = point
    return [(x + xoff, y + yoff) for xoff, yoff in offsets]


def get_white_tile_neighbors(point, tiles):
    neighbors = get_neighbors(point)
    return [x for x in neighbors if x not in tiles]


def get_black_tile_neighbors(point, tiles):
    neighbors = get_neighbors(point)
    return [x for x in neighbors if x in tiles]


def determine_black_to_white_tile_flip(tiles):
    to_flip = []
    for x in tiles:
        num_black_neighbor_tiles = len(get_black_tile_neighbors(x, tiles))
        if num_black_neighbor_tiles == 0 or num_black_neighbor_tiles > 2:
            to_flip.append(x)
    return to_flip


def determine_white_to_black_tile_flip(tiles):
    to_flip = []
    white_tile_black_neighbor_counts = {}
    for x in tiles:
        white_neighbor_tiles = get_white_tile_neighbors(x, tiles)
        for y in white_neighbor_tiles:
            if y in white_tile_black_neighbor_counts:
                white_tile_black_neighbor_counts[y] += 1
            else:
                white_tile_black_neighbor_counts[y] = 1
    
    for y in white_tile_black_neighbor_counts:
        if white_tile_black_neighbor_counts[y] == 2:
            to_flip.append(y)
                
    return to_flip


def do_step(tiles):
    w2b = determine_white_to_black_tile_flip(tiles)
    b2w = determine_black_to_white_tile_flip(tiles)

    # print(w2b)
    # print(b2w)

    for x in b2w:
        del tiles[x]
    
    for y in w2b:
        tiles[y] = 1
    
    return tiles
