from bisect import bisect_left

global input_no
global goal

# Hardcoded input
input_no = 1362
goal = (31, 39)

def allowed(x, y):
    if (x < 0) or (y < 0):
        return False
    val = x * x + 3 * x + 2 * x * y + y + y * y
    val += input_no
    number_of_ones = '{0:b}'.format(val).count('1')
    return number_of_ones % 2 == 0

class State:

    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps
        self.distance = ((goal[0] - x)**2 + (goal[1] - y)**2)**0.5 + steps

    def __repr__(self):
        return str((self.x, self.y))

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def done(self):
        return self.steps == self.distance

    def generate_next_states(self):
        states = []
        x_change = [1, -1, 0, 0]
        y_change = [0, 0, 1, -1]
        for x_ch, y_ch in zip(x_change, y_change):
            if allowed(self.x + x_ch, self.y + y_ch):
                states.append(State(self.x + x_ch, self.y + y_ch, self.steps + 1))
        return states

present_states = [State(1, 1, 0)]
past_states = {}
done = present_states[0].done()
count = 0
distances = [a.distance for a in present_states]
while not done:
    x = present_states.pop(0)
    y = distances.pop(0)
    if count % 10000 == 0:
        print('Current (count = {}) min distance {}'.format(count, y))
    past_states[x] = True
    new_states = x.generate_next_states()
    for z in new_states:
        if z not in past_states and z not in present_states:
            index = bisect_left(distances, z.distance)
            distances[index:index] = [z.distance]
            present_states[index:index] = [z]
            if z.done():
                done = True
                final = z
    count += 1
print('{} nodes expanded.'.format(count))
print('The minimum number of mooves is {}.'.format(final.steps))
