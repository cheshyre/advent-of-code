def rotate(cur_direction, rotation_command):
    # Assumes there are only R/L 90/180/270
    invert_rl = {
        "R": "L",
        "L": "R",
    }
    if int(rotation_command[1:]) == 270:
        rotation_command = f"{invert_rl[rotation_command[0]]}90"
        
    elif int(rotation_command[1:]) == 180:
        flip = {
            "N": "S",
            "E": "W",
            "S": "N",
            "W": "E",
        }
        return flip[cur_direction]
    
    lookup = {
        "L90" : {
            "N": "W",
            "E": "N",
            "S": "E",
            "W": "S",
        },
        "R90" : {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N",
        },
    }
    return lookup[rotation_command][cur_direction]


def rotate_waypoint(x, y, rotation_command):
    # Assumes there are only R/L 90/180/270
    invert_rl = {
        "R": "L",
        "L": "R",
    }
    if int(rotation_command[1:]) == 270:
        rotation_command = f"{invert_rl[rotation_command[0]]}90"
        
    elif int(rotation_command[1:]) == 180:
        return -1 * x, -1 * y
    
    if rotation_command == "L90":
        return -1 * y, x
    elif rotation_command == "R90":
        return y, -1 * x
    else:
        print(f"Invalid command: {rotation_command}")
        exit(-1)


def shift_coords(curx, cury, command):
    n = int(command[1:])
    offsets = {
        "N": (0, 1),
        "S": (0, -1),
        "W": (-1, 0),
        "E": (1, 0),
    }
    offx, offy = offsets[command[0]]
    return n * offx + curx, n * offy + cury


class Ship:
    
    def __init__(self):
        self.direction = "E"
        self.x = 0
        self.y = 0
        
    def run_command(self, command):
        if "L" in command or "R" in command:
            self.direction = rotate(self.direction, command)
        else:
            command = command.replace("F", self.direction)
            self.x, self.y = shift_coords(self.x, self.y, command)
        
    def manhattan_dist(self):
        return abs(self.x) + abs(self.y)


class ShipWithWaypoint:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
        
    def run_command(self, command):
        if "L" in command or "R" in command:
            self.waypoint_x, self.waypoint_y = rotate_waypoint(self.waypoint_x, self.waypoint_y, command)
        elif "F" in command:
            n = int(command[1:])
            self.x += self.waypoint_x * n
            self.y += self.waypoint_y * n
        else:
            self.waypoint_x, self.waypoint_y = shift_coords(self.waypoint_x, self.waypoint_y, command)
        
    def manhattan_dist(self):
        return abs(self.x) + abs(self.y)
            