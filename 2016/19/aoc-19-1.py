num_elves = 3014387

elves = [[1, i + 1] for i in range(num_elves)]

while len(elves) > 1:
    for i in range(len(elves)):
        if elves[i][0] != 0:
            elves[i][0] += elves[(i + 1) % len(elves)][0]
            elves[(i + 1) % len(elves)][0] = 0
    elves = [x for x in elves if x[0] != 0]

print('The elf with all the presents at the end is elf {}.'.format(elves[0][1]))
