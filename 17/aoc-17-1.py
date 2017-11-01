from hashlib import md5
from bisect import bisect_left

def get_doors(position, hash_str):
    doors = [False, False, False, False]
    door_open = ['b', 'c', 'd', 'e', 'f']
    conditions = [[1, 0], [1, 3], [0, 0], [0, 3]]
    for i, c in zip(range(4), conditions):
        doors[i] = hash_str[i] in door_open and position[c[0]] != c[1]
    return doors

def get_new_position(position, char):
    if char == 'U':
        return (position[0], position[1] - 1)
    elif char == 'D':
        return (position[0], position[1] + 1)
    elif char == 'L':
        return (position[0] - 1, position[1])
    else:
        return (position[0] + 1, position[1])

class Node:

    def __init__(self, x, y, path, passcode):
        self.position = (x, y)
        self.path = path
        self.hash = md5('{}{}'.format(passcode, path).encode('utf-8')).hexdigest()
        self.distance = len(path) + abs(3 - x) + abs(3 - y)
        self.passcode = passcode

    def at_goal(self):
        return self.position == (3, 3)

    def __eq__(self, other):
        return self.position == other.position and self.path == other.path

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '{} via {}'.format(self.position, self.path)

    def __hash__(self):
        return hash((self.position[0], self.position[1], self.path))

    def expand(self):
        new_nodes = []
        doors = get_doors(self.position, self.hash)
        directions = ['U', 'D', 'L', 'R']
        for valid, d in zip(doors, directions):
            if valid:
                new_position = get_new_position(self.position, d)
                new_nodes.append(Node(new_position[0], new_position[1], self.path + d, self.passcode))
        return new_nodes

# Hardcoded input
passcode = 'qzthpkfp'

present_states = [Node(0, 0, '', passcode)]
past_states = {}
done = False
count = 0
distances = [a.distance for a in present_states]
while not done:
    if len(present_states) == 0:
        print('All paths lead to dead ends.')
        exit()
    x = present_states.pop(0)
    y = distances.pop(0)
    if count % 10000 == 0:
        print('Current (count = {}) min distance {}'.format(count, y))
    past_states[x] = True
    new_states = x.expand()
    for z in new_states:
        if z not in past_states:
            index = bisect_left(distances, z.distance)
            distances[index:index] = [z.distance]
            present_states[index:index] = [z]
            if z.at_goal():
                done = True
                final = z
    count += 1
print('{} nodes expanded.'.format(count))
print('The shortest path is {}.'.format(final.path))
