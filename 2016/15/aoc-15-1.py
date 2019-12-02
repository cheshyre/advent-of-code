from sys import argv

class Disc:

    def __init__(self, no_positions, init_position, depth, time=0):
        self.n = no_positions
        self.p = init_position
        self.d = depth
        self.t = time

    def get_position(self, t):
        return (t - self.t + self.d + self.p) % self.n

def parse_input(string):
    string_tokens = string.split()
    depth = int(string_tokens[1][1:])
    positions = int(string_tokens[3])
    time = int(string_tokens[6].split('=')[1][:-1])
    init_position = int(string_tokens[-1][:-1])
    return Disc(positions, init_position, depth, time)

discs = []
with open(argv[1]) as f:
    for line in f:
        discs.append(parse_input(line))

time = 0
capsules_caught = []

while len(capsules_caught) == 0:
    if max([d.get_position(time) for d in discs]) == 0:
        capsules_caught.append(time)
    time += 1

print('You get your first capsule at t={}.'.format(capsules_caught[0]))
