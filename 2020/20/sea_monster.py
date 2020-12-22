def get_sea_monster():
    sea_monster = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   ",
    ]
    return sea_monster, len(sea_monster), len(sea_monster[0])

def mark_sea_monsters_at_coord(grid, x, y):
    sm, sm_y, sm_x = get_sea_monster()
    for yval in range(y, y + sm_y):
        for xval in range(x, x + sm_x):
            if sm[yval - y][xval - x] == "#" and grid[yval][xval] != "#":
                return False, grid
            
    for yval in range(y, y + sm_y):
        for xval in range(x, x + sm_x):
            if sm[yval - y][xval - x] == "#":
                grid[yval][xval] = "O"
    return True, grid


def mark_sea_monsters(grid):
    dimy = len(grid)
    dimx = len(grid[0])
    _, sm_y, sm_x = get_sea_monster()
    
    sm_found = False
    
    for y in range(dimy - sm_y):
        for x in range(dimx - sm_x):
            marked, grid = mark_sea_monsters_at_coord(grid, x, y)
            sm_found = sm_found or marked
    
    return sm_found, grid
