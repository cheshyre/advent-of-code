from bisect import bisect_left

global input_no
global goal

# Hardcoded input
input_no = 1362

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
count = 0
turns = 50
for i in range(turns):
    new_states = []
    for x in present_states:
        past_states[x] = True
        generated_states = x.generate_next_states()
        count += 1
        for y in generated_states:
            if y not in past_states and y not in present_states and y not in new_states:
                new_states.append(y)
    present_states = new_states
for x in present_states:
    past_states[x] = True

print('{} nodes expanded.'.format(count))
print('{} unique states reachable in {} turns.'.format(len(past_states), turns))
