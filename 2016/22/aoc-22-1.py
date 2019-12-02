from sys import argv

class Node:

    def __init__(self, size, used, position):
        self.size = size
        self.used = used
        self.position = position

    def __repr__(self):
        return '{}: {}/{}'.format(self.position, self.used, self.size)

def is_pair_valid(a, b):
    if a.used == 0:
        return False
    if a.position == b.position:
        return False
    if b.used + a.used > b.size:
        return False
    return True

filename = argv[1]

nodes = []

with open(filename) as f:
    for line in f:
        if 'dev' in line:
            tokens = line.split()
            x = int(tokens[0].split('-')[1][1:])
            y = int(tokens[0].split('-')[2][1:])
            size = int(tokens[1][:-1])
            used = int(tokens[2][:-1])
            nodes.append(Node(size, used, (x, y)))

valid_count = 0
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if is_pair_valid(nodes[i], nodes[j]):
            valid_count += 1

print('There are {} valid pairs.'.format(valid_count))
