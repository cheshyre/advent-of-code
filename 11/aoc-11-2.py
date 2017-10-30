from bisect import bisect_left


global num_levels
num_levels = 4
global kind_data
kind_data = ['C', 'G']
global elem_data

# Hardcoded Part 2 input
elem_data = ['Pm', 'Co', 'Cm', 'Ru', 'Pu', 'El', 'Dl']
init_state_data = [0, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0]

def calc_hash(chip_data, generator_data):
    a = [(chip_data[i], generator_data[i]) for i in range(len(chip_data))]
    a.sort(key=lambda x: num_levels * x[0] + x[1])
    value = sum([a[i][0] * num_levels ** (2 * i + 1) + a[i][1] * num_levels ** (2 * (i + 1)) for i in range(len(a))])
    return value

def check_state_validity(data):
    for i in range(int(len(data)/2)):
        if data[i] != data[i + int(len(data)/2)]:
            p = check_elem_validity(data[i], data[int(len(data)/2):])
            if not p:
                return False
    return True

def check_elem_validity(val, generator_data):
    for n in generator_data:
        if val == n:
            return False
    return True

class State:

    def __init__(self, pos_data, e_pos=0, turn=0):
        self.pos_data = list(pos_data)
        self.pos = e_pos
        self.turn = turn
        self.distance = turn + sum([num_levels - 1 - x for x in self.pos_data]) / 2
        self.hash = calc_hash(self.pos_data[:int(len(self.pos_data) / 2)], self.pos_data[int(len(self.pos_data) / 2):]) + e_pos

    def check_validity(self, i):
        generator_data = self.pos_data[int(len(self.pos_data) / 2):]
        if generator_data[i] == self.pos_data[i]:
            return True
        for j in range(len(generator_data)):
            if self.pos_data[i] == generator_data[j] and i != j:
                return False
        return True

    def is_complete(self):
        for val in self.pos_data:
            if val != num_levels - 1:
                return False
        return True

    def __repr__(self):
        data = ['{}{} {}'.format(elem_data[i % len(elem_data)], kind_data[int(i/len(elem_data))], self.pos_data[i]) for i in range(len(self.pos_data))]
        data_string = ', '.join(data)
        return 'pos: {} - data: {}'.format(self.pos, data_string)

    def __eq__(self, other):
        return self.hash == other.hash

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.hash)

    def generate_next_states(self):
        states = []
        for i in range(len(self.pos_data)):
            if self.pos_data[i] == self.pos:
                if self.pos < num_levels - 1:
                    pos_data_copy = list(self.pos_data)
                    pos_data_copy[i] += 1
                    if check_state_validity(pos_data_copy):
                        new_state = State(pos_data_copy, self.pos + 1, self.turn + 1)
                        if new_state not in states:
                            states.append(new_state)
                if min(self.pos_data) < self.pos:
                    pos_data_copy = list(self.pos_data)
                    pos_data_copy[i] += -1
                    if check_state_validity(pos_data_copy):
                        new_state = State(pos_data_copy, self.pos - 1, self.turn + 1)
                        if new_state not in states:
                            states.append(new_state)
                for j in range(i + 1, len(self.pos_data)):
                    if self.pos_data[i] == self.pos_data[j]:
                        if self.pos < num_levels - 1:
                            pos_data_copy = list(self.pos_data)
                            pos_data_copy[i] += 1
                            pos_data_copy[j] += 1
                            if check_state_validity(pos_data_copy):
                                new_state = State(pos_data_copy, self.pos + 1, self.turn + 1)
                                if new_state not in states:
                                    states.append(new_state)
                        if min(self.pos_data) < self.pos:
                            pos_data_copy = list(self.pos_data)
                            pos_data_copy[i] += -1
                            pos_data_copy[j] += -1
                            if check_state_validity(pos_data_copy):
                                new_state = State(pos_data_copy, self.pos - 1, self.turn + 1)
                                if new_state not in states:
                                    states.append(new_state)
        return states

present_states = [State(init_state_data)]
past_states = {}
done = False
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
        if z not in past_states:
            index = bisect_left(distances, z.distance)
            distances[index:index] = [z.distance]
            present_states[index:index] = [z]
            if z.is_complete():
                done = True
                final = z
    count += 1
print('{} nodes expanded.'.format(count))
print('The minimum number of mooves is {}.'.format(final.turn))

