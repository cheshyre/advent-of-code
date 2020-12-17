def get_neighbors(x, y, xmax, ymax):
    offsets = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    neighbors = []
    for xoff, yoff in offsets:
        xnew = x + xoff
        ynew = y + yoff
        if xnew >= 0 and xnew <= xmax and ynew >= 0 and ynew <= ymax:
            neighbors.append((xnew, ynew))

    return neighbors
        

def get_neighbors_los(x, y, xmax, ymax, grid):
    offsets = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    neighbors = []
    for xoff, yoff in offsets:
        for n in range(1, max(xmax, ymax) + 1):
            xnew = x + n * xoff
            ynew = y + n * yoff
            if xnew < 0 or xnew > xmax or ynew < 0 or ynew > ymax:
                break
            if grid[ynew][xnew] != ".":
                neighbors.append((xnew, ynew))
                break

    return neighbors
        

def output_value(x, y, grid):
    ymax = len(grid) - 1
    xmax = -1
    if ymax >= 0:
        xmax = len(grid[0]) - 1
    neighbors = get_neighbors(x, y, xmax, ymax)
    if grid[y][x] == ".":
        return "."
    occ_count = 0
    for xnew, ynew in neighbors:
        if grid[ynew][xnew] == "#":
            occ_count += 1
    
    if grid[y][x] == "L":
        if occ_count == 0:
            return "#"
        else:
            return "L"
    elif grid[y][x] == "#":
        if occ_count < 4:
            return "#"
        else:
            return "L"
    else:
        print(f"Invalid grid tile: {grid[y][x]}")
        exit(-1)
        

def output_value_los(x, y, grid):
    ymax = len(grid) - 1
    xmax = -1
    if ymax >= 0:
        xmax = len(grid[0]) - 1
    neighbors = get_neighbors_los(x, y, xmax, ymax, grid)
    if grid[y][x] == ".":
        return "."
    occ_count = 0
    for xnew, ynew in neighbors:
        if grid[ynew][xnew] == "#":
            occ_count += 1
    
    if grid[y][x] == "L":
        if occ_count == 0:
            return "#"
        else:
            return "L"
    elif grid[y][x] == "#":
        if occ_count < 5:
            return "#"
        else:
            return "L"
    else:
        print(f"Invalid grid tile: {grid[y][x]}")
        exit(-1)
        

def check_grid_equality(grid1, grid2):
    if grid1 is None:
        return False
    if grid2 is None:
        return False
    for row1, row2 in zip(grid1, grid2):
        for el1, el2 in zip(row1, row2):
            if el1 != el2:
                return False
            
    return True

def print_grid(grid):
    for x in grid:
        print("".join(x))
    print("\n")
        


class SeatingPlan:
    
    def __init__(self, starting_plan):
        self.prev_plan = None
        self.curr_plan = []
        for x in starting_plan:
            self.curr_plan.append(list(x))
            
        # print_grid(self.curr_plan)
        self.next_plan = None
        
    def do_step(self):
        ydim = len(self.curr_plan)
        xdim = 0
        if ydim > 0:
            xdim = len(self.curr_plan[0])
        self.next_plan = []
        for x in self.curr_plan:
            self.next_plan.append(list(x))
        for x in range(xdim):
            for y in range(ydim):
                self.next_plan[y][x] = output_value(x, y, self.curr_plan)
        # print_grid(self.next_plan)
                
        stable = False
        looping = False
        
        if check_grid_equality(self.curr_plan, self.next_plan):
            stable = True
        
        if not stable and check_grid_equality(self.prev_plan, self.next_plan):
            looping = True
            
        self.prev_plan = self.curr_plan
        self.curr_plan = self.next_plan
        self.next_plan = None
        
        return stable, looping
        
    def do_step_los(self):
        ydim = len(self.curr_plan)
        xdim = 0
        if ydim > 0:
            xdim = len(self.curr_plan[0])
        self.next_plan = []
        for x in self.curr_plan:
            self.next_plan.append(list(x))
        for x in range(xdim):
            for y in range(ydim):
                self.next_plan[y][x] = output_value_los(x, y, self.curr_plan)
        # print_grid(self.next_plan)
                
        stable = False
        looping = False
        
        if check_grid_equality(self.curr_plan, self.next_plan):
            stable = True
        
        if not stable and check_grid_equality(self.prev_plan, self.next_plan):
            looping = True
            
        self.prev_plan = self.curr_plan
        self.curr_plan = self.next_plan
        self.next_plan = None
        
        return stable, looping
        
    def count_occupied(self):
        ydim = len(self.curr_plan)
        xdim = 0
        if ydim > 0:
            xdim = len(self.curr_plan[0])
        occ_count = 0
        for x in range(xdim):
            for y in range(ydim):
                if self.curr_plan[y][x] == "#":
                    occ_count += 1
                    
        return occ_count
            
        