def determine_next_active_dict(active_dict):
    next_active_dict = {}
    inactive_neighbor_counts = {}
    ignored_coords = set()
    for coord in active_dict:
        if len(active_dict[coord].get_active_neighbors(active_dict)) in [2, 3]:
            next_active_dict[coord] = active_dict[coord]
        for new_coord in active_dict[coord].get_inactive_neighbors(active_dict):
            if new_coord not in ignored_coords:
                if new_coord in inactive_neighbor_counts:
                    inactive_neighbor_counts[new_coord] += 1
                    if inactive_neighbor_counts[new_coord] > 3:
                        del inactive_neighbor_counts[new_coord]
                        ignored_coords.add(new_coord)
                else:
                    inactive_neighbor_counts[new_coord] = 1
    for coord in inactive_neighbor_counts:
        if inactive_neighbor_counts[coord] == 3:
            next_active_dict[coord] = HyperCube(coord[0], coord[1], coord[2], coord[3])
    return next_active_dict


def draw_state(active_dict):
    min_x = min([x[0] for x in active_dict])
    min_y = min([x[1] for x in active_dict])
    min_z = min([x[2] for x in active_dict])
    min_w = min([x[3] for x in active_dict])
    max_x = max([x[0] for x in active_dict])
    max_y = max([x[1] for x in active_dict])
    max_z = max([x[2] for x in active_dict])
    max_w = max([x[3] for x in active_dict])
    
    for w in range(min_w, max_w + 1):
        for z in range(min_z, max_z + 1):
            print(f"z = {z}, w = {w}")
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if (x, y, z, w) in active_dict:
                        print("#", end="")
                    else:
                        print(".", end="")
                print("")
            print("")


class HyperCube:
    
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        
    def get_neighbors(self):
        offsets = [-1, 0, 1]
        neighbors = []
        for xoff in offsets:
            for yoff in offsets:
                for zoff in offsets:
                    for woff in offsets:
                        if yoff == 0 and xoff == 0 and zoff == 0 and woff == 0:
                            continue
                        neighbors.append((self.x + xoff, self.y + yoff, self.z + zoff, self.w + woff))
        return neighbors
    
    def get_active_neighbors(self, active_dict):
        neighbors = self.get_neighbors()
        return [x for x in neighbors if x in active_dict]
    
    def get_inactive_neighbors(self, active_dict):
        neighbors = self.get_neighbors()
        return [x for x in neighbors if x not in active_dict]
